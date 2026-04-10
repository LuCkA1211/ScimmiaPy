from abc import ABC, abstractmethod

class IAISelectCardStrategy(ABC):

    @abstractmethod
    def selectCardToPlay(self, aiPlayer):
        pass