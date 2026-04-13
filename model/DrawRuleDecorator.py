from model.IDrawRule import IDrawRule

class DrawRuleDecorator(IDrawRule):

    def __init__(self, innerComponent):
        self._innerComponent = innerComponent
        self._game = innerComponent.game()
    
    def draw(self):
        return self._innerComponent.draw()
    
    def game(self):
        return self._innerComponent.game()