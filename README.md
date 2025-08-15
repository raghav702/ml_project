# Student Performance Prediction ML Project

A complete Machine Learning pipeline for predicting student math scores based on various characteristics using Flask web application.

## 🎯 Project Overview

This project predicts student math scores using machine learning based on the following features:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

## 📁 Project Structure

```
Project/
├── app.py                          # Flask web application
├── test_pipeline.py                # Test script for the ML pipeline
├── templates/
│   └── index.html                  # Web interface template
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       # Data loading and splitting
│   │   ├── data_transformation.py  # Feature preprocessing
│   │   └── model_trainer.py        # Model training and evaluation
│   ├── pipeline/
│   │   ├── train_pipeline.py       # Complete training pipeline
│   │   └── predict_pipeline.py     # Prediction pipeline
│   ├── utils.py                    # Utility functions
│   ├── exception.py                # Custom exception handling
│   └── logger.py                   # Logging configuration
├── notebook/
│   ├── data/
│   │   └── stud.csv               # Student performance dataset
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
└── requirements.txt                # Python dependencies
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python src/pipeline/train_pipeline.py
```

### 3. Run the Web Application
```bash
python app.py
```

### 4. Open in Browser
Navigate to: `http://localhost:5000`

## 🎨 Features

### Web Application Features:
- **Beautiful Modern UI** with gradient backgrounds and smooth animations
- **Real-time Predictions** with instant feedback
- **Model Training** directly from the web interface
- **Responsive Design** that works on all devices
- **Input Validation** with helpful error messages
- **Loading States** with spinners and progress indicators

### ML Pipeline Features:
- **Automated Data Ingestion** with train/test splitting
- **Feature Engineering** with categorical encoding and scaling
- **Multiple Model Comparison** (Random Forest, XGBoost, CatBoost, etc.)
- **Hyperparameter Tuning** using GridSearchCV
- **Model Persistence** for easy deployment
- **Comprehensive Logging** for debugging

## 🔧 Usage

### Web Interface:
1. Fill in the student information form
2. Click "Predict Math Score" to get predictions
3. Click "Train Model" to retrain the model with latest data

### Programmatic Usage:
```python
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Create input data
data = CustomData(
    gender="female",
    race_ethnicity="group B",
    parental_level_of_education="bachelor's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=72,
    writing_score=74
)

# Make prediction
pipeline = PredictPipeline()
prediction = pipeline.predict(data.get_data_as_dataframe())
print(f"Predicted Math Score: {prediction[0]:.2f}")
```

## 🧪 Testing

Run the complete pipeline test:
```bash
python test_pipeline.py
```

This will:
- Test the training pipeline
- Test the prediction pipeline
- Provide detailed feedback on success/failure

## 📊 Model Performance

The pipeline automatically evaluates multiple models and selects the best performing one based on R² score. Typical performance metrics:
- **R² Score**: 0.85+ (varies based on data)
- **Models Tested**: Random Forest, XGBoost, CatBoost, Linear Regression, etc.
- **Cross-validation**: 3-fold CV for robust evaluation

## 🛠️ Technical Details

### Technologies Used:
- **Backend**: Python, Flask
- **ML Libraries**: Scikit-learn, XGBoost, CatBoost
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Data Processing**: Pandas, NumPy

### Key Components:
- **Data Ingestion**: Handles data loading and train/test splitting
- **Data Transformation**: Preprocesses features (encoding, scaling)
- **Model Training**: Trains multiple models and selects the best
- **Prediction Pipeline**: Loads trained model and makes predictions
- **Web Interface**: User-friendly form for input and results display

## 🔍 API Endpoints

- `GET /` - Main web interface
- `POST /predict` - Make predictions
- `POST /train` - Retrain the model

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For questions or issues, please open an issue on the repository.