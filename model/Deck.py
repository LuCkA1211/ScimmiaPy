from model.Card import Card
from model.SkipCard import SkipCard
from model.SwapCard import SwapCard
from model.Draw2Card import Draw2Card
from model.Draw4Card import Draw4Card
from model.NormalCard import NormalCard
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
        
        for k in range(self.__deckDesc.numberDraw2):
            d2c = Draw2Card()
            self.__cardsInDeck.append(d2c)
        
        for k in range(self.__deckDesc.numberDraw4):
            d4c = Draw4Card()
            self.__cardsInDeck.append(d4c)

        for k in range(self.__deckDesc.numberSkip):
            skip = SkipCard()
            self.__cardsInDeck.append(skip)

        for k in range(self.__deckDesc.numberSwap):
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
    
    def drawCards(self, cardsToDraw):
        cardsDrawn = []
        if(len(self.cardsInDeck) < cardsToDraw):
            cardsToDraw = len(self.cardsInDeck)
        for i in range(cardsToDraw):
            c = self.getTopCard()
            cardsDrawn.append(c)
        return cardsDrawn