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


from src.textSummarizer.pipeline.DataTransformation_Pipeline import DataTransformationTrainingPipeline
STAGE_NAME= "Data Transformation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} gets Initiated")

    data_transformation_pipeline= DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    
    logger.info(f"Stage {STAGE_NAME} has Completed")

except Exception as e:
    logger.exception(e)
    raise e


from src.textSummarizer.pipeline.ModelTrainer_Pipeline import ModelTrainerTrainingPipeline
STAGE_NAME= "Model Trainer Stage"
try:
    logger.info(f"Stage {STAGE_NAME} gets Initiated")

    model_trainer_pipeline= DataTransformationTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    
    logger.info(f"Stage {STAGE_NAME} has Completed")

except Exception as e:
    logger.exception(e)
    raise e


from src.textSummarizer.pipeline.ModelEvaluation_Pipeline import ModelEvaluationTrainingPipeline
STAGE_NAME= "Model Evaluation Stage"
try:

    logger.info(f"*******************")
    logger.info(f">>>>>> Stage {STAGE_NAME} gets Initiated <<<<<<")
   
    model_evaluation= ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>>>> Stage {STAGE_NAME} has Completed <<<<<<\n\nx==========x")
   
except Exception as e:
    logger.exception(e)
    raise e
