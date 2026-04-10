from model.Game import Game
from model.AIStandardGameSelectCardFactory import AIStandardGameSelectCardFactory
from model.AIPlayer import AIPlayer

class StandardGame(Game):

    def __init__(self, player, deckDesc, difficulty, numberCardsToDraw, penalty):
        super().__init__(player, deckDesc, difficulty, numberCardsToDraw, penalty)
        factory = AIStandardGameSelectCardFactory()
        aiPlayer = AIPlayer("AI1", factory, difficulty)
        self._players.append(aiPlayer)
    
    def checkEndGame(self):
        if(self._currentPlayer.noCardsInHand()):
            self._winner = self._currentPlayer
            self._isEnded = True
        elif(self._table.emptyDeck()):
            self._isEnded = True
            minNumberCards = 100
            for p in self._players:
                if(p.numberCardsInHand() < minNumberCards):
                    self._winner = p
                    minNumberCards = p.numberCardsInHand()