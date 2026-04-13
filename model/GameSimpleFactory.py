from model.PointGame import PointGame
from model.StandardGame import StandardGame

class GameSimpleFactory():

    __instance = None
    __initialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
    
    def createGame(self, player, difficulty, numberCardsToDraw, penalty, modality, deckDesc):
        if(modality == "Standard"):
            return StandardGame(player, deckDesc, difficulty, numberCardsToDraw, penalty)
        elif (modality == "Point"):
            return PointGame(player, deckDesc, difficulty, numberCardsToDraw, penalty)
        return None