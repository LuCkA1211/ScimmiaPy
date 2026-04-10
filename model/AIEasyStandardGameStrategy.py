from model.IAISelectCardStrategy import IAISelectCardStrategy
import random

class AIEasyStandardGameStrategy(IAISelectCardStrategy):

    def selectCardToPlay(self, aiPlayer):
        playableCards = aiPlayer.getPlayableCardsFromHand()
        return random.randrange(len(playableCards))