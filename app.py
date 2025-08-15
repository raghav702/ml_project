import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
import pickle
import os
from pathlib import Path
import sys

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from src.pipeline.predict_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

# Load the trained model and preprocessor
model_path = "artifact/model.pkl"
preprocessor_path = "artifact/preprocessor.pkl"

# Check if model files exist
if not os.path.exists(model_path) or not os.path.exists(preprocessor_path):
    print("⚠️  Model files not found! Please run the training pipeline first.")
    print("Run: python src/pipeline/train_pipeline.py")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form
        
        # Create CustomData object
        custom_data = CustomData(
            gender=data['gender'],
            race_ethnicity=data['race_ethnicity'],
            parental_level_of_education=data['parental_level_of_education'],
            lunch=data['lunch'],
            test_preparation_course=data['test_preparation_course'],
            reading_score=float(data['reading_score']),
            writing_score=float(data['writing_score'])
        )
        
        # Convert to dataframe
        df = custom_data.get_data_as_dataframe()
        
        # Make prediction
        pipeline = PredictPipeline()
        prediction = pipeline.predict(df)
        
        # Format the prediction
        predicted_score = round(prediction[0], 2)
        
        return jsonify({
            'success': True,
            'predicted_math_score': predicted_score,
            'message': f'Predicted Math Score: {predicted_score}'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/train', methods=['POST'])
def train_model():
    try:
        from src.pipeline.train_pipeline import TrainPipeline
        
        pipeline = TrainPipeline()
        r2_score = pipeline.run_pipeline()
        
        return jsonify({
            'success': True,
            'r2_score': round(r2_score, 4),
            'message': f'Model trained successfully! R² Score: {r2_score:.4f}'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
