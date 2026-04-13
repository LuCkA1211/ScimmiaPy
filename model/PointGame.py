from model.Game import Game
from model.AIPointGameSelectCardFactory import AIPointGameSelectCardFactory
from model.AIPlayer import AIPlayer

class PointGame(Game):

    __pointsToWin = 100

    def __init__(self, player, deckDesc, difficulty, numberCardsToDraw, penalty):
        super().__init__(player, deckDesc, difficulty, numberCardsToDraw, penalty)
        factory = AIPointGameSelectCardFactory()
        aiPlayer = AIPlayer("AI1", factory, difficulty)
        self.players.append(aiPlayer)
        self.__playerPoints = {}
        for p in self.players:
            self.__playerPoints[p] = 0
    
    @property
    def playerPoints(self):
        return self.__playerPoints
    
    @playerPoints.setter
    def playerPoints(self, playerPoints):
        self.__playerPoints = playerPoints

    def updatePlayerPoints(self, player, pointsToRemove):
        self.__playerPoints[player] = self.__playerPoints.get(player) + pointsToRemove
    
    def updatePoints(self):
        if(self.currentPlayer.hasPlayed):
            playedCard = self.table.faceUpCard
            self.updatePlayerPoints(self._currentPlayer, playedCard.value)
    
    def getSpecificPlayerPoints(self, player):
        return self.__playerPoints.get(player)
    
    def checkEndGame(self):
        pass