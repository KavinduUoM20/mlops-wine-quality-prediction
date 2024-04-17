from mlopsproject import logger
from mlopsproject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from mlopsproject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
# from mlopsproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from mlopsproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from mlopsproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
