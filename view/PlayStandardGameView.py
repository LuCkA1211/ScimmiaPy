from model.DeckDescription import DeckDescription
from model.GameSimpleFactory import GameSimpleFactory
from view.PlayGameView import PlayGameView

class PlayStandardGameView(PlayGameView):

    def __init__(self):
        super().__init__()
    
    def printRules(self):
        print()
        print("Stai giocando alla modalità standard")
    
    def startGame(self, player):
        gsf = GameSimpleFactory()
        deckDesc = DeckDescription(5,5,5,5)
        self.printDifficulty()
        difficulty = self.getDifficulty()
        self.printNumberCardsToDraw()
        numberCardsToDraw = self.getNumberCardsToDraw()
        sg = gsf.createGame(player, difficulty, numberCardsToDraw, "N", "Standard", deckDesc)
        self.game = sg
        self.play()
    
    def endTurn(self):
        self._game.passTurn()