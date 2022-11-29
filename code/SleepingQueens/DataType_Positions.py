from dataclasses import dataclass

@dataclass
class SleepingQueenPosition:
    _cardIndex: int

    def getCardIndex(self) -> int:
        return self._cardIndex
    
@dataclass
class HandPosition:
    _cardIndex: int
    _playerIndex: int

    def getCardIndex(self) -> int:
        return self._cardIndex
    
    def getPlayerIndex(self) -> int:
        return self._playerIndex

@dataclass
class AwokenQueenPostion:
    _cardIndex: int
    _playerIndex: int

    def getCardIndex(self) -> int:
        return self._cardIndex

    def getPlayerIndex(self) -> int:
        return self._playerIndex
