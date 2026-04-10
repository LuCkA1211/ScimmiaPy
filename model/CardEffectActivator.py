from model.NormalCard import NormalCard

class CardEffectActivator:

    def applyEffect(self, cardPlayed, currentPlayer, nextPlayer, deck):
        if(not(isinstance(cardPlayed, NormalCard))):
            cardPlayed.effect(currentPlayer, nextPlayer, deck)