from Game import Game
from Player import Player

class GameObservable:

    def addPlayer(playerIdx: int) -> None:
        if playerIdx not in range(1,6):
            raise "Invalid player index"
        
        if playerIdx - max(Game.players.keys()) != 1:
            raise "Invalid player index"

        Game.players[playerIdx] = Player()
    
    
    def getNumOfPlayers(self) -> int:
        return len(Game.players.keys())
