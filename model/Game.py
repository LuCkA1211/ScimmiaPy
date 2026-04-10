from abc import ABC, abstractmethod

from model.CardEffectActivator import CardEffectActivator
from model.Table import Table
from model.DrawRuleSimpleFactory import DrawRuleSimpleFactory

import random

class Game(ABC):

    def __init__(self, player, deckDesc, difficulty, numberCardsToDraw, penalty):
        self._numberStartingCards = 7
        player.clearHand()
        player.clearTurnState()
        self._players = []
        self._players.append(player)
        self._table = Table(deckDesc)
        self._cardEffectActivator = CardEffectActivator()
        self._winner = None
        self._isEnded = False
        self._indexPlayer = 0
        self._drawRule = None
        self.createAndSetDrawRule(numberCardsToDraw, penalty)
        self._currentPlayer = None
        self._nextPlayer = None

    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, players):
        self._players = players

    @property
    def table(self):
        return self._table
    
    @table.setter
    def players(self, table):
        self._table = table

    @property
    def isEnded(self):
        return self._isEnded
    
    @isEnded.setter
    def isEnded(self, isEnded):
        self._isEnded = isEnded
    
    @property
    def winner(self):
        return self._winner
    
    @winner.setter
    def winner(self, winner):
        self._winner = winner

    @property
    def currentPlayer(self):
        return self._currentPlayer
    
    @currentPlayer.setter
    def currentPlayer(self, currentPlayer):
        self._currentPlayer = currentPlayer
    
    @property
    def nextPlayer(self):
        return self._nextPlayer
    
    @nextPlayer.setter
    def nextPlayer(self, nextPlayer):
        self._nextPlayer = nextPlayer
    
    @property
    def drawRule(self):
        return self._drawRule
    
    @drawRule.setter
    def drawRule(self, drawRule):
        self._drawRule = drawRule

    def createAndSetDrawRule(self, numberCardsToDraw, penalty):
        self._drawRule = DrawRuleSimpleFactory().getDrawRule(numberCardsToDraw, penalty, self)
    
    def giveStartingCards(self):
        for p in self._players:
            startingCards = self._table.getCardsFromDeck(self._numberStartingCards)
            p.addCardsToHand(startingCards)
    
    def assignOrderPlayers(self):
        random.shuffle(self._players)
    
    def start(self):
        self.assignOrderPlayers()
        self.giveStartingCards()
        self._table.setFirstPlayableCard()
        return self._table.faceUpCard()
    
    def getFaceUpCard(self):
        return self._table.faceUpCard()
    
    @abstractmethod
    def checkEndGame(self):
        pass

    def assignPlayer(self):
        self._currentPlayer = self._players[self._indexPlayer]
        self._currentPlayer.hasPlayed(False)
        self._nextPlayer = self._players[(self._indexPlayer + 1) % len(self._players)]
        return self._currentPlayer.nickname()
    
    def getCardsInHand(self):
        return self._currentPlayer.getCardsInHand()
    
    def getPlayableCards(self):
        return self._currentPlayer.getPlayableCards(self._table)
    
    def playCardFromIndex(self, indexCard):
        self._currentPlayer.playCardFromIndex(indexCard, self._table)
        self.activateEffect()
    
    def activateEffect(self):
        faceUpCard = self.getFaceUpCard()
        deck = self._table.deck()
        self._cardEffectActivator.applyEffect(faceUpCard, self._currentPlayer, self._nextPlayer, deck)
    
    def draw(self):
        cardsDrawn = self._drawRule.draw()
        if(self._currentPlayer.hasPlayed()):
            self.activateEffect()
        return cardsDrawn
    
    def passTurn(self):
        self._currentPlayer.hasTakenTurn(False)
        self._indexPlayer = (self._indexPlayer + 1) % len(self._players)
        self.checkEndGame()
    
    def hasCurrentPlayerTakenTurn(self):
        return self._currentPlayer.hasTakenTurn()

    def hasCurrentPlayerPlayed(self):
        return self._currentPlayer.hasPlayed()
    
    def getNumberOfCardsInHand(self):
        numbercardsInHandPlayer = {}
        for p in self._players:
            numbercardsInHandPlayer[p] = len(p.getCardsInHand())
        return numbercardsInHandPlayer
    
    def getNumberOfCardsInDeck(self):
        return self._table.getNumberOfCardsInDeck()
    
    def drawCardChosenPlayer(self, p):
        return p.drawCard(self._table)
    