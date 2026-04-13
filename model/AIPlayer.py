from model.Player import Player

class AIPlayer(Player):
    
    def __init__(self, nickname, factory, difficulty):
        super().__init__(nickname)
        self.__selectCardStrategy = factory.createStrategy(difficulty)

    @property
    def selectCardStrategy(self):
        return self.__selectCardStrategy
    
    @selectCardStrategy.setter
    def selectCardStrategy(self, strategy):
        self.__selectCardStrategy = strategy
    
    def playCardFromIndex(self, indexCard, table):
        indexCardPlay = self.__selectCardStrategy.selectCardToPlay(self)
        cardToPlay = self.hand.getCardFromIndex(indexCardPlay)
        self.playCard(cardToPlay, table)
