from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
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
        logger.logging.info("Initiate the data Validation")
        data_validation_Artifact=data_validation.initiate_data_validation()
        logger.logging.info("Data Validation Complete")
        print(data_validation_Artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

