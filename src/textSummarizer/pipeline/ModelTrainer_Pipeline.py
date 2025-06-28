from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.ModelTrainer import ModelTrainer
from src.textSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config = ConfigurationManager()

        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(config= model_trainer_config)

        model_trainer.train()

