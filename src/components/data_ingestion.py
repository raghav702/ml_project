import os 
import sys 
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.exception import CustomException
from src.logger import logging

import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train.csv")
    test_data_path: str = os.path.join('artifact', "test.csv")
    raw_data_path: str = os.path.join('artifact', "data.csv")

class DataIngestion:
    def __init__(self, test_size=0.2, random_state=42):
        self.ingestion_config = DataIngestionConfig()
        self.test_size = test_size
        self.random_state = random_state

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Use artifact directory for data file
            data_path = os.path.join('artifact', 'stud.csv')
            
            # Check if source file exists
            if not os.path.exists(data_path):
                raise FileNotFoundError(f"Source data file not found: {data_path}")
            
            df = pd.read_csv(data_path)
            logging.info('Read the dataset as dataframe')
            
            # Basic data validation
            if df.empty:
                raise ValueError("Dataset is empty")
            
            logging.info(f"Dataset shape: {df.shape}")
            logging.info(f"Dataset columns: {list(df.columns)}")

            # Create artifact directory if it doesn't exist
            artifact_dir = os.path.dirname(self.ingestion_config.train_data_path)
            os.makedirs(artifact_dir, exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved to: {self.ingestion_config.raw_data_path}")

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(
                df, 
                test_size=self.test_size, 
                random_state=self.random_state
            )

            # Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info(f"Train set shape: {train_set.shape}")
            logging.info(f"Test set shape: {test_set.shape}")
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys) 
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()