from Player import Player
from typing import List

class Game:
    players: List[Player] = []

    def getNumOfPlayers(self) -> int:
        return len(self.players)

    def addPlayer(self, p: Player) -> None:
        self.players.append(p)