from Player import Player
from DrawingAndTrashPile import DrawingAndTrashPile
from typing import List, Dict, Position, Optional, Any
from GameObservable import GameObservable
from Queens import SleepingQueens, AwokenQueens
from QueenCollection import QueenCollection
from GameFinished import GameFinished
from GameState import GameState
from GameAdaptor import GameAdaptor

class Game:
    players: Dict[int, Player]
    currentTurn: int
    _turnOrder: List[int]
    piles: DrawingAndTrashPile
    sleepingQueens: SleepingQueens
    awokenQueens: AwokenQueens

    def __init__(self, numOfPlayers: int,otherDiscardPileMethod: bool = False) -> None:
        for i in range(1, numOfPlayers + 1):
            GameObservable.addPlayer(i)
        
        self.piles = DrawingAndTrashPile(otherDiscardPileMethod)
        self.sleepingQueens = SleepingQueens(shuffle=False)
        self.awokenQueens = AwokenQueens()
        self.piles.dealCardsToPlayers()
        turnOrder: List[int] = [range(1, numOfPlayers + 1)]
        
        while not GameFinished.isFinished():
            self.currentTurn = self.getTurn()
            command = GameAdaptor.getGameArguments()
            gS: GameState = self.play(self.currentTurn -1, command[0], command[1], command[2])
            print(GameState)

        print(f'Player {GameFinished.whoWon} won the Game ! Congrats!')
        return
    
    def play(self, playerIdx: int, cards: List[Any], targetQueen: Any, targetPlayerIdx: int) -> Optional[GameState]:
        Game.players[playerIdx].play(cards, targetQueen, targetPlayerIdx)


    def getTurn(self) -> int:
        turn = self._turnOrder.pop(0)
        self._turnOrder.append(turn)
        return turn
