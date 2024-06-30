from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject import logger




STAGE_NAME = "Data Ingestion Pipeline"


class DataIngestionTrainingPipeline:

    def __init__(self):
        pass
    

    def main(self):
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ =="__main__":
    try:
        logger.info(STAGE_NAME)
        data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline.main()
        logger.info(STAGE_NAME + " completed successfully")
    except Exception as e:
        logger.error(STAGE_NAME + " failed")
        logger.exception(e)
        raise e



