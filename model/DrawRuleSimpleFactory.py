from model.ChosenNumberDrawRuleDecorator import ChosenNumberDrawRuleDecorator
from model.BaseDrawRule import BaseDrawRule
from model.PenaltyOnDrawnCardsDrawRuleDecorator import PenaltyOnDrawnCardsDrawRuleDecorator
from model.UnlimitedDrawRuleDecorator import UnlimitedDrawRuleDecorator

class DrawRuleSimpleFactory():

    __instance = None
    __initialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
        
    def getDrawRule(self, numberCardsToDraw, penalty, game):
        drawRule = BaseDrawRule(game)

        if(numberCardsToDraw > 1):
            drawRule = ChosenNumberDrawRuleDecorator(drawRule, numberCardsToDraw)
        elif(numberCardsToDraw == -1):
            drawRule = UnlimitedDrawRuleDecorator(drawRule)
        
        if(penalty == "Y"):
            drawRule = PenaltyOnDrawnCardsDrawRuleDecorator(drawRule)

        return drawRule