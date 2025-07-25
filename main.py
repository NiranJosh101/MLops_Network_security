from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_tranformation import DataTransformation
from networksecurity.components.model_training import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainPipelineConfig()

        # Data Ingestion
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logger.logging.info("<<======Initiate the data ingestion=======>>")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logger.logging.info("Data Ingestion Complete")
        print(dataingestionartifact)

        # Data validation
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logger.logging.info("<<======Initiate the data Validation=======>>")
        data_validation_Artifact=data_validation.initiate_data_validation()
        logger.logging.info("Data Validation Complete")
        print(data_validation_Artifact)

        # Data transformation
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_Artifact,data_transformation_config)
        logger.logging.info("<<======Initiate the data Transformation=======>>")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logger.logging.info("Data Transformation Complete")
        print(data_transformation_artifact)

        # Model Training
        logger.logging.info("Model Training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logger.logging.info("Model Training artifact created")

    except Exception as e:
        raise NetworkSecurityException(e, sys)

