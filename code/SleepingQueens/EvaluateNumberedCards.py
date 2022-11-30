from Cards import Card
from typing import List


class EvaluateNumberedCards:

    def __init__(self, cards: List[Card]) -> None:
        self.cards: List[Card] = cards

    def play(self) -> bool:
        numOfCards: int = len(self.cards)
        if numOfCards == 2:
            return self.cards[0].value == self.cards[1].value
        else:
            eq: List[Card] = sorted(self.cards, key = lambda x: x.value)
            sum: int = 0
            for card in eq[:-1]:
                sum += card.value

            return sum == eq[-1].value
