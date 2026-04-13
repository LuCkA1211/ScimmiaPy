from model.IDrawRule import IDrawRule

class BaseDrawRule(IDrawRule):

    def __init__(self, game):
        self.__game = game

    def draw(self):
        cardsDrawn = []
        cardDrawn = self.__game.drawCardChosenPlayer(self.__game.currentPlayer())
        cardsDrawn.append(cardDrawn)
        return cardsDrawn
    
    def game(self):
        return self.__game