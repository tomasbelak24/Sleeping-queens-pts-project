from dataclasses import dataclass
from enum import Enum


class CardType(Enum):
    NUMBER = 1
    KING = 2
    KNIGHT = 3
    SLEEPING_POTION = 4
    DRAGON = 5
    MAGIC_WAND = 6


@dataclass
class Queen:
    points: int
    name: str


@dataclass
class Card:
    type: CardType
    value: int

