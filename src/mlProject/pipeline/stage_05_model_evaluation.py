from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
    def __init__ (self):
        pass

    def main (self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config = model_evaluation_config)
            model_evaluation.save_results()

        except Exception as e:
            raise