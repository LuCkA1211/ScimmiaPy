from model.DrawRuleDecorator import DrawRuleDecorator

class PenaltyOnDrawnCardsDrawRuleDecorator(DrawRuleDecorator):

    _penaltyWeight = 5
    
    def __init__(self, innerComponent):
        super().__init__(innerComponent)

    def draw(self):
        drawnCards = self._innerComponent.draw()
        drawnCards =self.addedBehaviour(drawnCards)
        return drawnCards
    
    def addedBehaviour(self, drawnCards):
        currentPlayerPoints = self._game.getSpecificPlayerPoints(self._game.currentPlayer())
        pointsToRemove = len(drawnCards) * self._penaltyWeight
        if(pointsToRemove > currentPlayerPoints):
            pointsToRemove = currentPlayerPoints
        self._game.updatePlayerPoints(self.game.currentPlayer(), -pointsToRemove)