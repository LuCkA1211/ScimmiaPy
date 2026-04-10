from model.NormalCard import NormalCard


class Hand:

    def __init__(self):
        self.__cardsInHand = []
        self.__playableCards = []
        self.__lastFaceUpCard = None
    
    @property
    def cardsInHand(self):
        return self.__cardsInHand
    
    @cardsInHand.setter
    def cardsInHand(self, cardsInHand):
        self.__cardsInHand = cardsInHand
    
    @property
    def playableCards(self):
        return self.__playableCards
    
    @playableCards.setter
    def playableCards(self, playableCards):
        self.__playableCards = playableCards

    @property
    def lastFaceUpCard(self):
        return self.__lastFaceUpCard
    
    @lastFaceUpCard.setter
    def lastFaceUpCard(self, lastFaceUpCard):
        self.__lastFaceUpCard = lastFaceUpCard
        self.updatePlayableCards()

    def addCard(self, card):
        self.__cardsInHand.append(card)
    
    def addCards(self, cards):
        self.__cardsInHand.extend(cards)
    
    def removeCard(self, card):
        self.__cardsInHand.remove(card)
    
    def getCardFromIndex(self, index):
        return self.__playableCards[index]
    
    def isPlayable(self, card):
        if(card is None):
            return False
        if(self.__lastFaceUpCard.color == "Black"):
            return True
        faceUpCardColor = self.__lastFaceUpCard.color()
        faceUpCardValue = self.__lastFaceUpCard.value()
        if((card.color() == faceUpCardColor) or (card.value() == faceUpCardValue) or (not(isinstance(card, NormalCard)))):
            return True