from model.DeckDescription import DeckDescription
from model.GameSimpleFactory import GameSimpleFactory
from view.PlayGameView import PlayGameView

class PlayPointGameView(PlayGameView):

    def __init__(self):
        super().__init__()
    
    def printPenalty(self):
        print("Vuoi inserire la penalità di 5 punti per ogni carta pescata? Y se sì, N altrimenti")
    
    def getPenalty(self):
        return input()
    
    def printActualPoints(self, playerPoints):
        print("I punteggi attuali sono: ")
        for pKey, points in playerPoints.items():
            print(f"{pKey.nickname}: {points}")
    
    def printRules(self):
        print()
        print("Stai giocando alla modalità a punti")
    
    def endTurn(self):
        self._game.passTurn()
        playerPoints = self.game.playerPoints
        self.printActualPoints(playerPoints)
    
    def startGame(self, player):
        gsf = GameSimpleFactory()
        deckDesc = DeckDescription(5,5,5,5)
        self.printDifficulty()
        difficulty = self.getDifficulty()
        self.printNumberCardsToDraw()
        numberCardsToDraw = self.getNumberCardsToDraw()
        self.printPenalty()
        penalty = self.getPenalty()
        pg = gsf.createGame(player, difficulty, numberCardsToDraw, penalty, "Point", deckDesc)
        self.game = pg
        self.play()