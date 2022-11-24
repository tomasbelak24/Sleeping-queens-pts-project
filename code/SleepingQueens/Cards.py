from dataclasses import dataclass
from enum import Enum


@dataclass
class CardType():
    _cardTypes = ["NUMBER",
                  "KING",
                  "KNIGHT",
                  "SLEEPING_POTION",
                  "DRAGON",
                  "MAGIC_WAND"]


@dataclass
class Queen:
    points: int
    name: str


@dataclass
class Card:
    type: CardType
    value: int

