from interfaces import PlayerInterface
class MoveQueen:

    def playKing(targetQueen: int, player: PlayerInterface) -> bool:
        try:
            player.awokenQueens.addQueen(player.game.sleepingQueens.removeQueen(targetQueen))
        except:
            return False
        return True


    def playKnight(targetQueen: int, targetPlayerIdx: int, player: PlayerInterface) -> bool:
        try:
            player.awokenQueens.addQueen(
                player.game.players[targetPlayerIdx].awokenQueens.removeQueen(targetQueen))
        except:
            return False
        return True
    

    def playSleepingPotion(targetQueen: int, targetPlayerIdx: int, player: PlayerInterface) -> bool:
        try:
            player.game.sleepingQueens.addQueen(
                player.game.players[targetPlayerIdx].awokenQueens.removeQueen(targetQueen))
        except:
            return False
        return True
