from model.DrawRuleDecorator import DrawRuleDecorator

class UnlimitedDrawRuleDecorator(DrawRuleDecorator):

    def __init__(self, innerComponent):
        super().__init__(innerComponent)

    def draw(self):
        drawnCards = self._innerComponent.draw()
        drawnCards =self.addedBehaviour(drawnCards)
        return drawnCards
    
    def addedBehaviour(self, drawnCards):
        while(not(self._game.hasCurrentPlayerPlayed())):
            cardDrawn = self._innerComponent.draw()
            if(cardDrawn[0] is None):
                return drawnCards
            drawnCards.extend(cardDrawn)
            return drawnCards