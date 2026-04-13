from model.Hand import Hand
from model.Player import Player

class HumanPlayer(Player):
    
    def __init__(self, nickname):
        super().__init__(nickname)
    
    def playCardFromIndex(self, indexCardPlay, table):
        cardToBePlayed = self.hand.getCardFromIndex(indexCardPlay)
        self.playCard(cardToBePlayed, table)
    
    def clearHand(self):
        self.hand = Hand()
    
    def clearTurnState(self):
        self.hasPlayed = False
        self.hasTakenTurn = False