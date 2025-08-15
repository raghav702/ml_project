#!/usr/bin/env python3
"""
Startup script for the Student Performance Predictor Flask App
"""

import os
import sys
from pathlib import Path

def check_model_files():
    """Check if model files exist"""
    model_path = "artifact/model.pkl"
    preprocessor_path = "artifact/preprocessor.pkl"
    
    if not os.path.exists(model_path) or not os.path.exists(preprocessor_path):
        print("⚠️  Model files not found!")
        print("Training the model first...")
        
        try:
            from src.pipeline.train_pipeline import TrainPipeline
            pipeline = TrainPipeline()
            r2_score = pipeline.run_pipeline()
            print(f"✅ Model trained successfully! R² Score: {r2_score:.4f}")
            return True
        except Exception as e:
            print(f"❌ Model training failed: {str(e)}")
            return False
    else:
        print("✅ Model files found!")
        return True

def main():
    print("🚀 Starting Student Performance Predictor...")
    print("=" * 50)
    
    # Check if model is trained
    if not check_model_files():
        print("❌ Cannot start application without trained model.")
        sys.exit(1)
    
    print("\n🌐 Starting Flask web application...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Import and run Flask app
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
