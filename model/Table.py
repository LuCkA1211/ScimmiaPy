from model.Deck import Deck

class Table:

    def __init__(self, deckDesc):
        self.__deck = Deck(deckDesc)
        self.__faceUpCard = None
    
    @property
    def deck(self):
        return self.__deck
    
    @deck.setter
    def deck(self, deck):
        self.__deck = deck
    
    @property
    def faceUpCard(self):
        return self.__faceUpCard
    
    @faceUpCard.setter
    def faceUpCard(self, faceUpCard):
        self.__faceUpCard = faceUpCard
    
    def getCardsFromDeck(self, numberCards):
        return self.__deck.drawCards(numberCards)
    
    def drawCardFromDeck(self):
        return self.__deck.getTopCard()
    
    def emptyDeck(self):
        return any(self.__deck.getCardsInDeck())
    
    def setFirstPlayableCard(self):
        firstPlayableCard = self.__deck.getTopCard()
        self.faceUpCard(firstPlayableCard)
    
    def playCard(self, card):
        self.faceUpCard(card)
    
    def getNumberOfCardsInDeck(self):
        return len(self.__deck.getCardsInDeck())