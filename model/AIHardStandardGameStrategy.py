from model.IAISelectCardStrategy import IAISelectCardStrategy
from model.NormalCard import NormalCard
import random

class AIHardStandardGameStrategy(IAISelectCardStrategy):

    def selectCardToPlay(self, aiPlayer):
        playableCards = aiPlayer.getPlayableCardsFromHand()

        if(len(playableCards) == 1):
            return 0

        for c in playableCards:
            if(not(isinstance(c, NormalCard))):
                return playableCards.index(c)
            
        lastFaceUpCard = aiPlayer.getLastFaceUpCard()
        cardsInHand = aiPlayer.getCardsInHand()

        colorCardsInHandDict = {}
        valueCardsInHandDict = {}
        playableCardsForColor = []
        playableCardsForValue = []

        self.splitPlayableCards(playableCards, playableCardsForColor, playableCardsForValue, lastFaceUpCard)
        self.computeOccurencies(colorCardsInHandDict, valueCardsInHandDict, cardsInHand)

        if(not(isinstance(lastFaceUpCard, NormalCard))):
            return random.randrange(len(playableCards))
        
        colorOccurence = colorCardsInHandDict.get(lastFaceUpCard.color(), 0)
        valueOccurence = valueCardsInHandDict.get(lastFaceUpCard.value(), 0)

        if valueOccurence >= colorOccurence and playableCardsForValue:
            cardToPlay = random.choice(playableCardsForValue)
        else:
            cardToPlay = random.choice(playableCardsForColor)

        return playableCards.index(cardToPlay)

    def splitPlayableCards(self, playableCards, playableCardsForColor, playableCardsForValue, lastFaceUpCard):
        for c in playableCards:
            if c.color() == lastFaceUpCard.color:
                playableCardsForColor.append(c)
            if c.value() == lastFaceUpCard.value:
                playableCardsForValue.append(c)

    def computeOccurencies(self, colorCardsInHandDict, valueCardsInHandDict, cardsInHand):
        for c in cardsInHand:
            color = c.color
            value = c.value

            colorCardsInHandDict[color] = colorCardsInHandDict.get(color, 0) + 1
            valueCardsInHandDict[value] = valueCardsInHandDict.get(value, 0) + 1

    def splitPlayableCards(self, playableCards, playableCardsForColor, playableCardsForValue, lastFaceUpCard):
        for c in playableCards:
            if(c.color() == lastFaceUpCard.color):
                playableCardsForColor.append(c)
            if(c.value() == lastFaceUpCard.value):
                playableCardsForValue.append(c)
    
    def computeOccurencies(self, colorCardsInHandDict, valueCardsInHandDict, cardsInHand):
        for c in cardsInHand:
            color = c.color
            value = c.value

            colorCardsInHandDict[color] = colorCardsInHandDict.get(color, 0) + 1
            valueCardsInHandDict[value] = valueCardsInHandDict.get(value, 0) + 1