from view.PlayPointGameView import PlayPointGameView
from view.PlayStandardGameView import PlayStandardGameView

class MenuView:

    def printMenu(self, player):
        print(f"Bentornato {player.nickname}")
        print("Cosa vuoi fare oggi?")
        print("1) Standard Game")
        print("2) Point Game")
        print("Se vuoi uscire inserisci un numero diverso")
        print("Inserisci il numero sequenziale")
    
    def getMenuChoice(self):
        indexMenu = int(input())
        return indexMenu
    
    def printExitGame(self):
        print("Ciao! Alla prossima!")
    
    def startScimmia(self, player):
        sgView = PlayStandardGameView()
        pgView = PlayPointGameView()
        stopScimmia = False
        while(not(stopScimmia)):
            
            self.printMenu(player)
            indexMenu = self.getMenuChoice()
            
            if(indexMenu == 1):
                sgView.startGame(player)
            elif(indexMenu == 2):
                pgView.startGame(player)
            else:
                self.printExitGame()
                stopScimmia = True