from model.DrawRuleDecorator import DrawRuleDecorator

class ChosenNumberDrawRuleDecorator(DrawRuleDecorator):

    def __init__(self, innerComponent, maxCardsToDraw):
        super().__init__(innerComponent)
        self._maxCardsToDraw = maxCardsToDraw
    
    def draw(self):
        drawnCards = self._innerComponent.draw()
        drawnCards = self.addedBehaviour(drawnCards)
        return drawnCards
    
    def addedBehaviour(self, drawnCards):
        while(not(self._game.hasCurrentPlayerPlayed()) and (len(drawnCards) < self._maxCardsToDraw)):
            cardDrawn = self._innerComponent.draw()
            if(cardDrawn[0] is None):
                return drawnCards
            drawnCards.extend(cardDrawn)
            return drawnCards