from model.Card import Card

class Draw2Card(Card):

    def __init__(self):
        super().__init__(10, "Black")

    def __str__(self):
        return "Draw_2"
    
    def descriptionEffect(self):
        return "Il prossimo giocatore pesca due carte"
    
    def effect(self, currentPlayer, nextPlayer, deck):
        cardsDrawn = deck.drawCards(2)
        nextPlayer.addCardsToHand(cardsDrawn)