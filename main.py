from src.textSummarizer.logging import logger

logger.info("Logging has succcessfully implemented")


from src.textSummarizer.pipeline.DataIngestion_Pipeline import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} gets Initiated")

    data_ingestion_pipeline= DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    
    logger.info(f"Stage {STAGE_NAME} has Completed")

except Exception as e:
    logger.exception(e)
    raise e

