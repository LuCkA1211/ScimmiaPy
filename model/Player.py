from abc import ABC, abstractmethod
from model.Hand import Hand

class Player(ABC):

    def __init__(self, nickname):
        self.__hand = Hand()
        self.__nickname = nickname
        self.__hasPlayed = False
        self.__hasTakenTurn = False

    @property
    def hand(self):
        return self.__hand
    
    @hand.setter
    def hand(self, hand):
        self.__hand = hand
    
    @property
    def nickname(self):
        return self.__nickname
    
    @nickname.setter
    def nickname(self, nickname):
        self.__nickname = nickname

    @property
    def hasPlayed(self):
        return self.__hasPlayed
    
    @hasPlayed.setter
    def hasPlayed(self, hasPlayed):
        self.__hasPlayed = hasPlayed
    
    @property
    def hasTakenTurn(self):
        return self.__hasTakenTurn

    @hasTakenTurn.setter
    def hasTakenTurn(self, hasTakenTurn):
        self.__hasTakenTurn = hasTakenTurn
    
    def addCardsToHand(self, cardToBeAdded):
        self.__hand.addCards(cardToBeAdded)
    
    @abstractmethod
    def playCardFromIndex(self, indexCard, table):
        pass

    def startTurn(self):
        self.__hasPlayed = False
        self.__hasTakenTurn = True

    def getPlayableCards(self, table):
        faceUpCard = table.faceUpCard
        self.__hand.lastFaceUpCard = faceUpCard
        return self.getPlayableCardsFromHand()
    
    def getCardsInHand(self):
        return self.__hand.cardsInHand
    
    def getPlayableCardsFromHand(self):
        return self.__hand.playableCards
    
    def setCardsInHand(self, cards):
        self.__hand.cardsInHand = cards
    
    def drawCard(self, table):
        drawnCard = table.drawCardFromDeck()
        self.handleDrawnCard(drawnCard, table)
        return drawnCard
    
    def isDrawnCardPlayable(self, drawnCard):
        return self.__hand.isPlayable(drawnCard)
    
    def playCard(self, cardToBePlayed, table):
        table.playCard(cardToBePlayed)
        self.__hasPlayed = True
        self.__hand.removeCard(cardToBePlayed)
    
    def handleDrawnCard(self, drawnCard, table):
        self.__hand.addCard(drawnCard)
        if(self.__hand.isPlayable(drawnCard)):
            self.playCard(drawnCard, table)
    
    def noCardsInHand(self):
        return any(self.__hand.cardsInHand)
    
    def numberCardsInHand(self):
        return len(self.__hand.cardsInHand)
    
    def getLastFaceUpCard(self):
        return self.__hand.lastFaceUpCard
    
    