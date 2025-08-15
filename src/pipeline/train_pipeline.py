import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def run_pipeline(self):
        try:
            logging.info("Starting the training pipeline")
            
            # Step 1: Data Ingestion
            logging.info("Step 1: Data Ingestion")
            train_path, test_path = self.data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed. Train: {train_path}, Test: {test_path}")
            
            # Step 2: Data Transformation
            logging.info("Step 2: Data Transformation")
            train_array, test_array, preprocessor_path = self.data_transformation.initiate_data_transformation(
                train_path=train_path,
                test_path=test_path
            )
            logging.info(f"Data transformation completed. Preprocessor saved to: {preprocessor_path}")
            
            # Step 3: Model Training
            logging.info("Step 3: Model Training")
            r2_score = self.model_trainer.initiate_model_trainer(
                train_array=train_array,
                test_array=test_array
            )
            logging.info(f"Model training completed. R2 Score: {r2_score}")
            
            logging.info("Training pipeline completed successfully!")
            return r2_score
            
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    pipeline = TrainPipeline()
    r2_score = pipeline.run_pipeline()
    print(f"Training completed with R2 Score: {r2_score}")
