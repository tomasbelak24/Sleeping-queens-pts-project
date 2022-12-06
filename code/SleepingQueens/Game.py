from Player import Player
from DrawingAndTrashPile import DrawingAndTrashPile
from typing import List, Dict, Optional, Any
from GameObservable import GameObservable
from Queens import SleepingQueens, AwokenQueens
from GameFinished import GameFinished
from GameState import GameState
from GameAdaptor import GameAdaptor

class Game:
    players: Dict[int, Player]
    currentTurn: int
    _turnOrder: List[int]
    piles: DrawingAndTrashPile
    sleepingQueens: SleepingQueens
    #awokenQueens: AwokenQueens
    otherDiscardPileMethod: bool

    def __init__(self, numOfPlayers: int,otherDiscardPileMethod: bool = False) -> None:
        for i in range(1, numOfPlayers + 1):
            GameObservable.addPlayer(i)
        self.otherDiscardPileMethod = otherDiscardPileMethod
        GameState.numberOfPlayers = numOfPlayers
        self.piles = DrawingAndTrashPile(self.otherDiscardPileMethod)
        self.sleepingQueens = SleepingQueens(shuffle=False)
        self.awokenQueens = AwokenQueens()
        turnOrder: List[int] = [range(1, numOfPlayers + 1)]
        
    def game(self):

        self.dealCardsToPlayers()
        
        while not GameFinished.isFinished():
            self.currentTurn = self.getTurn()
            command = GameAdaptor.getGameArguments()
            gS: GameState = self.play(self.currentTurn, command[0], command[1], command[2])
            print(gS)

        print(f'Player {GameFinished.whoWon} won the Game ! Congrats!')
        return
    
    def play(self, playerIdx: int, cards: List[Any], targetQueen: Any, targetPlayerIdx: int) -> Optional[GameState]:
        self.players[playerIdx].play(cards, targetQueen, targetPlayerIdx)


    def getTurn(self) -> int:
        turn = self._turnOrder.pop(0)
        self._turnOrder.append(turn)
        return turn
    
    def dealCardsToPlayers(self) -> None:
        for playerIdx in self.players.keys():
            for handPos in range(5):
                self.players[playerIdx].playerHand[handPos] = self.piles._drawingPile.pop(
                    0)
