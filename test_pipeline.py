#!/usr/bin/env python3
"""
Test script to verify the complete ML pipeline
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

def test_training_pipeline():
    """Test the complete training pipeline"""
    print("Testing Training Pipeline...")
    try:
        pipeline = TrainPipeline()
        r2_score = pipeline.run_pipeline()
        print(f"✅ Training completed successfully!")
        print(f"📊 R2 Score: {r2_score:.4f}")
        return True
    except Exception as e:
        print(f"❌ Training failed: {str(e)}")
        return False

def test_prediction_pipeline():
    """Test the prediction pipeline"""
    print("\nTesting Prediction Pipeline...")
    try:
        # Create sample data
        custom_data = CustomData(
            gender="female",
            race_ethnicity="group B",
            parental_level_of_education="bachelor's degree",
            lunch="standard",
            test_preparation_course="none",
            reading_score=72,
            writing_score=74
        )
        
        df = custom_data.get_data_as_dataframe()
        pipeline = PredictPipeline()
        prediction = pipeline.predict(df)
        
        print(f"✅ Prediction completed successfully!")
        print(f"🎯 Predicted Math Score: {prediction[0]:.2f}")
        return True
    except Exception as e:
        print(f"❌ Prediction failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Starting ML Pipeline Tests...\n")
    
    # Test training pipeline
    training_success = test_training_pipeline()
    
    # Test prediction pipeline (only if training was successful)
    if training_success:
        prediction_success = test_prediction_pipeline()
    else:
        print("\n⏭️  Skipping prediction test due to training failure")
        prediction_success = False
    
    # Summary
    print("\n" + "="*50)
    print("📋 TEST SUMMARY")
    print("="*50)
    print(f"Training Pipeline: {'✅ PASS' if training_success else '❌ FAIL'}")
    print(f"Prediction Pipeline: {'✅ PASS' if prediction_success else '❌ FAIL'}")
    
    if training_success and prediction_success:
        print("\n🎉 All tests passed! Your ML pipeline is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Please check the error messages above.")
