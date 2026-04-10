from model.IAISelectCardStrategy import IAISelectCardStrategy
import random
class AIEasyPointGameStrategy(IAISelectCardStrategy):

    def selectCardToPlay(self, aiPlayer):
        playableCards = aiPlayer.getPlayableCardsFromHand()
        sortedPlayableCards = sorted(playableCards, key=lambda x: x.value(), reverse=False)
        weights = [0 for _ in range(len(playableCards))]
        sumCoefficients = 0
        self.computeWeights(weights, sumCoefficients)
        randomNumber = random.random()
        maxIndex = self.findElement(weights, randomNumber)
        cardToPlay = sortedPlayableCards[maxIndex]
        index = playableCards.index(cardToPlay)
        return index

    
    def normalizeWeights(self, weights, sumCoefficients):
        for i in range(len(weights)):
            weights[i] /= sumCoefficients
    
    def findElement(self, weights, randomNumber):
        maxIndex = 0
        for i in range(len(weights)):
            if(weights[i] < randomNumber):
                maxIndex = i
            else:
                break
        return maxIndex
    
    def computeWeights(self, weights, sumCoefficients):
        for i in range(len(weights)):
            weights[i] = i + 1
            sumCoefficients += weights[i]