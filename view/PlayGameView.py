from abc import ABC, abstractmethod
from model.Game import Game
from model.HumanPlayer import HumanPlayer

class PlayGameView(ABC):

    def __init__(self):
        self._game = None

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game

    @abstractmethod
    def printRules(self):
        pass

    def printFaceUpCard(self, card):
        print(f"La faceUpCard attuale è {str(card)}")
    
    def printCurrentPlayer(self, nickname):
        print(f"Tocca a {nickname}")
    
    def printPassTurn(self):
        print("Passo il turno")

    def printWinner(self, p):
        print(f"The winner is {p.nickname}")
        print()
    
    def printPlayerCard(self, c):
        print(f"è stata giocata la carta {str(c)}")
    
    def printCards(self, cardsInHand):
        counter = 1
        for c in cardsInHand:
            print(f"{counter}) {str(c)}")
            counter += 1
        print()
    
    def printPlayableCards(self, playableCards):
        if(not(any(playableCards))):
            print("Non hai carte giocabili, devi pescare")
        else:
            print("Le tue playable cards sono: ")
            self.printCards(playableCards)
            print("Quale carta giochi? Inserisci il numero sequenziale")
    
    def printDifficulty(self):
        print("Seleziona la difficoltà")
        print("1) Easy")
        print("2) Hard")
    
    def printNumberCardsToDraw(self):
        print("Inserisci il numero di carte massimo da pescare quando non hai carte giocabili")
        print("Se non vuoi avere limiti, inserisci -1")
    
    def getPlayableCard(self):
        return int(input()) - 1
    
    def verifyInputPlayableCard(self, numberPlayableCards, indexCardPlay):
        if (((indexCardPlay + 1) <= 0) or ((indexCardPlay + 1) > numberPlayableCards)):
            return False
        return True
    
    def printErrorIndexPlayableCard(self):
        print("Inserisci un indice valido!")
    
    def getDifficulty(self):
        difficultyInt = int(input())
        difficultyMap = {
            1: "Easy",
            2: "Hard"
        }
        return difficultyMap[difficultyInt]
    
    def getNumberCardsToDraw(self):
        return int(input())
    
    def printDrawnCards(self, drawnCards):
        strToPrint = "Hai pescato: "
        for i in range(len(drawnCards)):
            strToPrint += str(drawnCards[i])
            if((len(drawnCards) != 1) and (i != (len(drawnCards) - 1))):
                strToPrint += ", "
        print(strToPrint)
        print()
    
    def printEffect(self, cardPlayed):
        print(cardPlayed.descriptionEffect())
        print()
    
    @abstractmethod
    def startGame(self, player):
        pass

    def printNumberCardsInHand(self):
        print("Carte in mano di ogni giocatore")
        numberCardsPlayer = self._game.getNumberOfCardsInHand()
        for pKey, nCards in numberCardsPlayer.items():
            print(f"{pKey.nickname}: {nCards}")

    def printRemainingCardsDeck(self):
        print("Carte rimanenti nel deck: ")
        print(self._game.getNumberOfCardsInDeck())
        print()

    def printGameState(self):
        self.printNumberCardsInHand()
        self.printRemainingCardsDeck()
    
    @abstractmethod
    def endTurn(self):
        pass
    
    def takeTurn(self):
        indexCard = 0
        nicknameCurrentPlayer = self._game.assignPlayer()
        if(not(self._game.hasCurrentPlayerTakenTurn())):
            self.printCurrentPlayer(nicknameCurrentPlayer)
            cardsInHand = self._game.getCardsInHand()
            playableCards = self._game.getPlayableCards()
            if(isinstance(self._game.currentPlayer, HumanPlayer)):
                self.printCards(cardsInHand)
                self.printPlayableCards(playableCards)
            if playableCards:
                if(isinstance(self._game.currentPlayer, HumanPlayer)):
                    while True:
                        indexCard = self.getPlayableCard()
                        if(self.verifyInputPlayableCard(len(playableCards), indexCard)):
                            break
                        else:
                            self.printErrorIndexPlayableCard()
                self._game.playCardFromIndex(indexCard)
            else:
                drawnCards = self._game.draw()
                if(isinstance(self._game.currentPlayer, HumanPlayer)):
                    self.printDrawnCards(drawnCards)
            if(self._game.hasCurrentPlayerPlayed()):
                cardPlayed = self._game.getFaceUpCard()
                self.printPlayerCard(cardPlayed)
                self.printEffect(cardPlayed)
        self.endTurn()

    def play(self):
        self.printRules()
        faceUpCard = self._game.start()
        self.printFaceUpCard(faceUpCard)
        while(not(self._game.isEnded)):
            self.printGameState()
            self.takeTurn()
        winner = self._game.winner
        self.printWinner(winner)
    