from Cards import Card
from typing import List
from interfaces import EvaluateNumberedCardsInterface


class EvaluateNumberedCards(EvaluateNumberedCardsInterface):

    def play(self, cards: List[Card]) -> bool:
        numOfCards: int = len(cards)
        if numOfCards == 2:
            return cards[0].value == cards[1].value
        else:
            eq: List[Card] = sorted(cards, key = lambda x: x.value)
            sum: int = 0
            for card in eq[:-1]:
                sum += card.value

            return sum == eq[-1].value
