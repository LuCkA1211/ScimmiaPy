from model import Card, SkipCard, SwapCard, Draw2Card, Draw4Card, NormalCard
from model.DeckDescription import DeckDescription
import random

class Deck:

    minCardValue = 1
    maxCardValue = 10
    numberCopyNormalCard = 3

    def __init__(self, deckDesc):
        self.__deckDesc = deckDesc
        self.__cardsInDeck = []
        colors = ["Red", "Blue", "Green", "Yellow"]
        for color in colors:
            for i in range(self.minCardValue, self.maxCardValue, 1):
                for j in range(self.numberCopyNormalCard):
                    nc = NormalCard(i, color)
                    self.__cardsInDeck.append(nc)
        
        for k in range(self.__deckDesc.numberDraw2()):
            d2c = Draw2Card()
            self.__cardsInDeck.append(d2c)
        
        for k in range(self.__deckDesc.numberDraw4()):
            d4c = Draw4Card()
            self.__cardsInDeck.append(d4c)

        for k in range(self.__deckDesc.numberDraw2()):
            skip = SkipCard()
            self.__cardsInDeck.append(skip)

        for k in range(self.__deckDesc.numberDraw2()):
            swap = SwapCard()
            self.__cardsInDeck.append(swap)
        
        self.shuffle()
    
    @property
    def cardsInDeck(self):
        return self.__cardsInDeck

    @cardsInDeck.setter
    def cardsInDeck(self, cardsInDeck):
        self.__cardsInDeck = cardsInDeck

    def shuffle(self):
        random.shuffle(self.__cardsInDeck)

    def getTopCard(self):
        if(not(any(self.__cardsInDeck))):
            return None
        return self.__cardsInDeck.pop()
