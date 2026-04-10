from abc import ABC, abstractmethod

class Card(ABC):

    def __init__(self, value, color):
        self.__value = value
        self.__color = color
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
    
    @abstractmethod
    def effect(self, currentPlayer, nextPlayer, deck):
        pass

    @abstractmethod
    def descriptionEffect(self):
        pass