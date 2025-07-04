from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.ModelEvaluation import ModelEvaluation
from src.textSummarizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()

        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config= model_evaluation_config)

        model_evaluation_config.evaluate()
        