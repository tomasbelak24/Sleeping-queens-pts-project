from Queens import SleepingQueens, AwokenQueens
from QueenCollection import QueenCollection
from Player import Player

class MoveQueen:

    def playKing(targetQueen: int, player: Player) -> bool:
        try:
            player.awokenQueens.addQueen(player.game.sleepingQueens.removeQueen(targetQueen))
        except:
            return False
        return True


    def playKnight(targetQueen: int, targetPlayerIdx: int, player: Player) -> bool:
        try:
            player.awokenQueens.addQueen(
                player.game.players[targetPlayerIdx].awokenQueens.removeQueen(targetQueen))
        except:
            return False
        return True
    

    def playSleepingPotion(targetQueen: int, targetPlayerIdx: int, player: Player) -> bool:
        try:
            player.game.sleepingQueens.addQueen(
                player.game.players[targetPlayerIdx].awokenQueens.removeQueen(targetQueen))
        except:
            return False
        return True
