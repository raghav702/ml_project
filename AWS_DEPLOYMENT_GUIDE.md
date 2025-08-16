# 🚀 AWS Deployment Guide for Student Performance Predictor

This guide will help you deploy your Flask ML application to AWS using different methods.

## 📋 Prerequisites

1. **AWS Account** - Sign up at [aws.amazon.com](https://aws.amazon.com)
2. **AWS CLI** - Install from [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
3. **AWS Credentials** - Configure with `aws configure`

## 🎯 Deployment Options

### Option 1: AWS Elastic Beanstalk (Recommended) ⭐

**Pros:** Easy deployment, automatic scaling, managed infrastructure
**Cons:** Less control over infrastructure

#### Step-by-Step:

1. **Install EB CLI:**
   ```bash
   pip install awsebcli
   ```

2. **Run Deployment Script:**
   ```bash
   python deploy_to_aws.py
   ```

3. **Manual Deployment (Alternative):**
   ```bash
   # Initialize EB application
   eb init --platform python-3.11
   
   # Create environment
   eb create student-performance-predictor
   
   # Deploy
   eb deploy
   ```

### Option 2: AWS EC2 (Manual Control)

**Pros:** Full control, cost-effective for small applications
**Cons:** Manual setup, more maintenance

#### Step-by-Step:

1. **Launch EC2 Instance:**
   - Choose Ubuntu Server 22.04 LTS
   - t2.micro (free tier) or t3.small
   - Configure security group to allow port 5000

2. **Connect to Instance:**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install Dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```

4. **Clone/Upload Code:**
   ```bash
   git clone your-repository-url
   # or upload via SCP
   ```

5. **Install Python Dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Train Model:**
   ```bash
   python3 src/pipeline/train_pipeline.py
   ```

7. **Run Application:**
   ```bash
   python3 app.py
   ```

### Option 3: Docker on AWS ECS/Fargate

**Pros:** Containerized, scalable, consistent environment
**Cons:** More complex setup

#### Step-by-Step:

1. **Build Docker Image:**
   ```bash
   docker build -t student-performance-app .
   ```

2. **Test Locally:**
   ```bash
   docker-compose up
   ```

3. **Push to ECR:**
   ```bash
   aws ecr create-repository --repository-name student-performance-app
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account-id.dkr.ecr.us-east-1.amazonaws.com
   docker tag student-performance-app:latest your-account-id.dkr.ecr.us-east-1.amazonaws.com/student-performance-app:latest
   docker push your-account-id.dkr.ecr.us-east-1.amazonaws.com/student-performance-app:latest
   ```

4. **Deploy to ECS:**
   - Create ECS cluster
   - Create task definition
   - Create service

## 🔧 Configuration Files

### Elastic Beanstalk Configuration
- `.ebextensions/01_flask.config` - Flask configuration
- `Procfile` - Process definition
- `requirements.txt` - Python dependencies

### Docker Configuration
- `Dockerfile` - Container definition
- `docker-compose.yml` - Local development

## 💰 Cost Estimation

### Elastic Beanstalk:
- **Free Tier:** 750 hours/month for t2.micro
- **Paid:** ~$15-30/month for t3.small

### EC2:
- **Free Tier:** 750 hours/month for t2.micro
- **Paid:** ~$10-20/month for t3.small

### ECS Fargate:
- **Free Tier:** 2 million requests/month
- **Paid:** ~$20-40/month for small workloads

## 🔒 Security Considerations

1. **HTTPS:** Use AWS Certificate Manager for SSL
2. **Environment Variables:** Store secrets in AWS Systems Manager
3. **IAM Roles:** Use least privilege principle
4. **Security Groups:** Restrict access to necessary ports only

## 📊 Monitoring & Logging

### CloudWatch Integration:
```python
import boto3
import logging

# Add to your app.py
cloudwatch = boto3.client('cloudwatch')

def log_prediction(prediction, features):
    cloudwatch.put_metric_data(
        Namespace='StudentPerformance',
        MetricData=[
            {
                'MetricName': 'Prediction',
                'Value': prediction,
                'Unit': 'None'
            }
        ]
    )
```

## 🚀 Quick Start Commands

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train model
python src/pipeline/train_pipeline.py

# 3. Test locally
python app.py

# 4. Deploy to AWS
python deploy_to_aws.py
```

## 🆘 Troubleshooting

### Common Issues:

1. **Port 5000 not accessible:**
   - Check security groups
   - Verify application is running

2. **Model files not found:**
   - Ensure model is trained before deployment
   - Check artifact directory exists

3. **Dependencies missing:**
   - Verify requirements.txt is complete
   - Check Python version compatibility

### Support:
- AWS Documentation: [docs.aws.amazon.com](https://docs.aws.amazon.com)
- Flask Documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)

## 🎉 Success!

Once deployed, your application will be available at:
- **Elastic Beanstalk:** `http://your-app-name.region.elasticbeanstalk.com`
- **EC2:** `http://your-ec2-public-ip:5000`
- **ECS:** `http://your-alb-dns-name`

Your ML application is now live on AWS! 🚀
