#!/usr/bin/env python3
"""
AWS Deployment Script for Student Performance Predictor
"""

import os
import sys
import subprocess
import zipfile
from pathlib import Path

def check_dependencies():
    """Check if AWS CLI is installed"""
    try:
        subprocess.run(['aws', '--version'], check=True, capture_output=True)
        print("✅ AWS CLI is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ AWS CLI not found. Please install it first:")
        print("   https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html")
        return False

def train_model():
    """Train the model before deployment"""
    print("🔧 Training model for deployment...")
    try:
        from src.pipeline.train_pipeline import TrainPipeline
        pipeline = TrainPipeline()
        r2_score = pipeline.run_pipeline()
        print(f"✅ Model trained successfully! R² Score: {r2_score:.4f}")
        return True
    except Exception as e:
        print(f"❌ Model training failed: {str(e)}")
        return False

def create_deployment_package():
    """Create a deployment package"""
    print("📦 Creating deployment package...")
    
    # Files to include in deployment
    files_to_include = [
        'app.py',
        'requirements.txt',
        'Procfile',
        '.ebextensions/',
        'src/',
        'templates/',
        'artifact/',
        'README.md'
    ]
    
    # Create deployment directory
    deploy_dir = 'deployment'
    if os.path.exists(deploy_dir):
        import shutil
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Copy files
    for item in files_to_include:
        src = Path(item)
        dst = Path(deploy_dir) / item
        
        if src.is_file():
            os.makedirs(dst.parent, exist_ok=True)
            import shutil
            shutil.copy2(src, dst)
        elif src.is_dir():
            import shutil
            shutil.copytree(src, dst)
    
    print(f"✅ Deployment package created in '{deploy_dir}' directory")
    return deploy_dir

def deploy_to_elastic_beanstalk(deploy_dir):
    """Deploy to AWS Elastic Beanstalk"""
    print("🚀 Deploying to AWS Elastic Beanstalk...")
    
    # Change to deployment directory
    os.chdir(deploy_dir)
    
    try:
        # Initialize EB application (if not already done)
        print("📋 Initializing Elastic Beanstalk application...")
        subprocess.run(['eb', 'init', '--platform', 'python-3.11'], check=True)
        
        # Create environment
        print("🌍 Creating Elastic Beanstalk environment...")
        subprocess.run(['eb', 'create', 'student-performance-predictor'], check=True)
        
        # Deploy
        print("📤 Deploying application...")
        subprocess.run(['eb', 'deploy'], check=True)
        
        print("✅ Deployment successful!")
        print("🌐 Your application is now live on AWS!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {str(e)}")
        return False
    
    return True

def deploy_to_ec2():
    """Deploy to AWS EC2"""
    print("🚀 Deploying to AWS EC2...")
    print("📋 This requires manual setup. Here are the steps:")
    print("1. Launch an EC2 instance with Ubuntu")
    print("2. Install Python, pip, and required packages")
    print("3. Upload your code using SCP or Git")
    print("4. Install dependencies: pip install -r requirements.txt")
    print("5. Run: python app.py")
    print("6. Configure security groups to allow port 5000")

def main():
    print("🚀 AWS Deployment Script for Student Performance Predictor")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Train model
    if not train_model():
        print("❌ Cannot deploy without trained model")
        return
    
    # Create deployment package
    deploy_dir = create_deployment_package()
    
    # Ask user for deployment method
    print("\n🎯 Choose deployment method:")
    print("1. AWS Elastic Beanstalk (Recommended)")
    print("2. AWS EC2 (Manual setup)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        deploy_to_elastic_beanstalk(deploy_dir)
    elif choice == "2":
        deploy_to_ec2()
    elif choice == "3":
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
