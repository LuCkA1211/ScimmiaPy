class DeckDescription:
    
    def __init__(self, numberDraw2, numberDraw4, numberSkip, numberSwap):
        self.__numberDraw2 = numberDraw2
        self.__numberDraw4 = numberDraw4
        self.__numberSkip = numberSkip
        self.__numberSwap = numberSwap

    @property
    def numberDraw2(self):
        return self.__numberDraw2
    
    @property
    def numberDraw4(self):
        return self.__numberDraw4
    
    @property
    def numberSkip(self):
        return self.__numberSkip
    
    @property
    def numberSwap(self):
        return self.__numberSwap