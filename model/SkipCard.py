from model.Card import Card

class SkipCard(Card):

    def __init__(self):
        super().__init__(10, "Black")

    def __str__(self):
        return "Skip"
    
    def descriptionEffect(self):
        return "Il prossimo giocatore non gioca il prossimo turno"
    
    def effect(self, currentPlayer, nextPlayer, deck):
        nextPlayer.hasTurnTaken(True)