from Player import Player
from DrawingAndTrashPile import DrawingAndTrashPile
from typing import List, Dict, Optional, Any
from Queens import SleepingQueens, AwokenQueens
from GameFinished import GameFinished
from GameState import GameState
from GameAdaptor import GameAdaptor
from interfaces import GameInterface
from Hand import Hand
from DrawingPileMethods import DrawingPileMethod

class Game(GameFinished, GameAdaptor, GameInterface):
    players: Dict[int, Player] = dict()
    currentTurn: int
    _turnOrder: List[int]
    piles: DrawingAndTrashPile
    sleepingQueens: SleepingQueens
    #awokenQueens: AwokenQueens

    def __init__(self, numOfPlayers: int,discardPileMethod: DrawingPileMethod = DrawingPileMethod.drawingPileMethod1) -> None:
        self.piles = DrawingAndTrashPile(False, discardPileMethod)
        for i in range(numOfPlayers):
            self.addPlayer(i)
        self.discardPileMethod = discardPileMethod
        self.numberOfPlayers = numOfPlayers
        self.sleepingQueens = SleepingQueens()
        self.awokenQueens = AwokenQueens()
        turnOrder: List[int] = [range(numOfPlayers)]
        
    def game(self):

        self.dealCardsToPlayers()
        
        while not self.isFinished():
            self.currentTurn: int = self.getTurn()
            command: List = self.getGameArguments()
            gS: GameState = self.play(self.currentTurn, command[0], command[1], command[2])
            print(gS)

        print(f'Player {self.whoWon} won the Game ! Congrats!')
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
                self.players[playerIdx].playerHand._hand[handPos] = self.piles.drawingPile.pop(0)


    def addPlayer(self, playerIdx: int) -> None:
        if playerIdx not in range(5):
            raise "Invalid player index"

        try:
            if playerIdx - max(self.players.keys()) != 1:
                raise "Invalid player index"
        except:
            pass

        self.players[playerIdx] = Player(game = self, playerHand = Hand(playerIdx, drawing = self.piles))
