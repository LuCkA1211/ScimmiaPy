from model.IAISelectCardStrategy import IAISelectCardStrategy

class AIHardPointGameStrategy(IAISelectCardStrategy):
    
    def selectCardToPlay(self, aiPlayer):
        playableCards = aiPlayer.getPlayableCardsFromHand()
        maxCardIndex = 0
        max = -1
        for i in range(len(playableCards)):
            if(playableCards[i].value() > max):
                max = playableCards[i].value()
                maxCardIndex = i
        return maxCardIndex