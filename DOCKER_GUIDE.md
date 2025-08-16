# 🐳 Docker Guide for Student Performance Predictor

This guide will help you use Docker with your Flask ML application.

## 📋 Prerequisites

1. **Docker Desktop** - Download from [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. **Windows 10/11** with WSL 2 enabled
3. **Virtualization** enabled in BIOS

## 🚀 Quick Start

### Step 1: Install Docker Desktop
1. Download Docker Desktop for Windows
2. Run the installer
3. Restart your computer
4. Start Docker Desktop

### Step 2: Test Docker Installation
```bash
python docker-test.py
```

### Step 3: Build and Run
```bash
# Build the Docker image
docker build -t student-performance-app .

# Run the container
docker run -p 5000:5000 student-performance-app
```

## 🎯 Docker Commands

### Basic Commands
```bash
# Build image
docker build -t student-performance-app .

# Run container
docker run -p 5000:5000 student-performance-app

# Run in background
docker run -d -p 5000:5000 --name my-app student-performance-app

# Stop container
docker stop my-app

# Remove container
docker rm my-app

# View logs
docker logs my-app

# List containers
docker ps

# List images
docker images
```

### Docker Compose (Recommended)
```bash
# Start with docker-compose
docker-compose up

# Start in background
docker-compose up -d

# Stop
docker-compose down

# Rebuild and start
docker-compose up --build
```

## 🔧 Dockerfile Explanation

```dockerfile
# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create artifact directory
RUN mkdir -p artifact

# Train the model during build
RUN python src/pipeline/train_pipeline.py

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

## 🐳 Docker Compose Explanation

```yaml
version: '3.8'

services:
  student-performance-app:
    build: .                    # Build from Dockerfile
    ports:
      - "5000:5000"            # Map port 5000
    environment:
      - FLASK_ENV=production   # Set environment
    volumes:
      - ./artifact:/app/artifact  # Persist model files
    restart: unless-stopped    # Auto-restart
```

## 🚀 Deployment Options

### Option 1: Local Development
```bash
# Run locally with Docker
docker-compose up

# Access at: http://localhost:5000
```

### Option 2: AWS ECS/Fargate
```bash
# Build and push to ECR
aws ecr create-repository --repository-name student-performance-app
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account.dkr.ecr.us-east-1.amazonaws.com
docker tag student-performance-app:latest your-account.dkr.ecr.us-east-1.amazonaws.com/student-performance-app:latest
docker push your-account.dkr.ecr.us-east-1.amazonaws.com/student-performance-app:latest
```

### Option 3: Google Cloud Run
```bash
# Build and push to GCR
docker tag student-performance-app gcr.io/your-project/student-performance-app
docker push gcr.io/your-project/student-performance-app

# Deploy to Cloud Run
gcloud run deploy student-performance-app --image gcr.io/your-project/student-performance-app --platform managed
```

## 🔍 Troubleshooting

### Common Issues:

1. **Docker not starting:**
   - Check if virtualization is enabled in BIOS
   - Ensure WSL 2 is installed
   - Restart Docker Desktop

2. **Port already in use:**
   ```bash
   # Find what's using port 5000
   netstat -ano | findstr :5000
   
   # Kill the process
   taskkill /PID <process_id> /F
   ```

3. **Build fails:**
   ```bash
   # Clean Docker cache
   docker system prune -a
   
   # Rebuild without cache
   docker build --no-cache -t student-performance-app .
   ```

4. **Container exits immediately:**
   ```bash
   # Check logs
   docker logs student-performance-app
   
   # Run interactively
   docker run -it student-performance-app /bin/bash
   ```

## 📊 Benefits of Using Docker

### ✅ Consistency
- Same environment everywhere
- No "works on my machine" issues

### ✅ Portability
- Run on any system with Docker
- Easy deployment to cloud platforms

### ✅ Isolation
- App runs in isolated container
- No conflicts with system packages

### ✅ Scalability
- Easy to scale horizontally
- Load balancing support

### ✅ Version Control
- Environment is version controlled
- Reproducible builds

## 🎉 Success!

Once Docker is working, you can:
- ✅ Run your app consistently
- ✅ Deploy to any cloud platform
- ✅ Scale easily
- ✅ Share with team members

Your ML application is now containerized and ready for production! 🚀

