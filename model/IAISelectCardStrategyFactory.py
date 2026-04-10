from abc import ABC, abstractmethod

class IAISelectCardStrategyFactory(ABC):

    @abstractmethod
    def createStrategy(self, difficulty):
        pass