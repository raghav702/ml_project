import sys
import pandas as pd
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        self.model_path = "artifact/model.pkl"
        self.preprocessor_path = "artifact/preprocessor.pkl"
        
    def predict(self, features):
        try:
            # Load the trained model and preprocessor
            model = load_object(file_path=self.model_path)
            preprocessor = load_object(file_path=self.preprocessor_path)
            
            # Transform the input features
            transformed_features = preprocessor.transform(features)
            
            # Make prediction
            prediction = model.predict(transformed_features)
            
            return prediction
            
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education, 
                 lunch, test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            
            return pd.DataFrame(custom_data_input_dict)
            
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    # Example usage
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
    print(f"Predicted Math Score: {prediction[0]:.2f}")
