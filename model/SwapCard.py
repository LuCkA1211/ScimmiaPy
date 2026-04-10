from model.Card import Card

class SwapCard(Card):

    def __init__(self):
        super().__init__(10, "Black")

    def __str__(self):
        return "Swap"
    
    def descriptionEffect(self):
        return "Scambia le carte con il prossimo giocatore"
    
    def effect(self, currentPlayer, nextPlayer, deck):
        currentPlayerCards = currentPlayer.getCardsInHand()
        nextPlayerCards = nextPlayer.getCardsInHand()
        currentPlayer.setCardsInHand(nextPlayerCards)
        nextPlayer.setCardsInHand(currentPlayerCards)