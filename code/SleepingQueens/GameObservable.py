from interfaces import GameInterface
from Player import Player

class GameObservable:

    def addPlayer(self,playerIdx: int, game: GameInterface) -> None:
        self.game = game
        if playerIdx not in range(1,6):
            raise "Invalid player index"
        
        if playerIdx - max(game.players.keys()) != 1:
            raise "Invalid player index"

        game.players[playerIdx] = Player(game)
    
    
    def getNumOfPlayers(self) -> int:
        return len(self.game.players.keys())
