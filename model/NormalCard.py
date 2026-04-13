from model.Card import Card

class NormalCard(Card):
    
    def __init__(self, value, color):
        super().__init__(value, color)

    def __str__(self):
        return f"{self.color} {self.value}"
    
    def descriptionEffect(self):
        return "Questa carta non ha particolari effetti"
    
    def effect(self, currentPlayer, nextPlayer, deck):
        pass