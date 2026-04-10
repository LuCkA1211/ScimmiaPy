from model.AIEasyPointGameStrategy import AIEasyPointGameStrategy
from model.AIHardPointGameStrategy import AIHardPointGameStrategy
from model.IAISelectCardStrategyFactory import IAISelectCardStrategyFactory

class AIPointGameSelectCardFactory(IAISelectCardStrategyFactory):

    __instance = None
    __initialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
        
    def createStrategy(self, difficulty):
        if difficulty == "Easy":
            return AIEasyPointGameStrategy()
        elif difficulty == "Hard":
            return AIHardPointGameStrategy()
        else:
            return None
