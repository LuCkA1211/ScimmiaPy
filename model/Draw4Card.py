from model.Card import Card

class Draw4Card(Card):

    def __init__(self):
        super().__init__(10, "Black")

    def __str__(self):
        return "Draw_4"
    
    def descriptionEffect(self):
        return "Il prossimo giocatore pesca quattro carte"
    
    def effect(self, currentPlayer, nextPlayer, deck):
        cardsDrawn = deck.drawCards(4)
        nextPlayer.addCardsToHand(cardsDrawn)