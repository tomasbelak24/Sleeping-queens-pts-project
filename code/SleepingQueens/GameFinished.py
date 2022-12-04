from Game import Game
from Player import Player
from GameState import GameState
from typing import List

class GameFinished:

    whoWon: int
    
    def isFinished(self) -> bool :
        for playerIdx in Game.players.keys():
            player = Game.players[playerIdx]
            aQueens = player.awokenQueens.values()
            if GameState.numberOfPlayers in [2,3]:
                if len(aQueens) == 5:
                    self.whoWon = playerIdx
                    return True
                else:
                    sumOfPoints = 0
                    for aQ in aQueens:
                        sumOfPoints += aQ.getPoints()
                    if sumOfPoints >= 50:
                        self.whoWon = playerIdx
                    return True
            if GameState.numberOfPlayers in [4, 5]:
                if len(aQueens) == 4:
                    self.whoWon = playerIdx
                    return True
                else:
                    sumOfPoints = 0
                    for aQ in aQueens:
                        sumOfPoints += aQ.getPoints()
                    if sumOfPoints >= 40:
                        self.whoWon = playerIdx
                    return True

