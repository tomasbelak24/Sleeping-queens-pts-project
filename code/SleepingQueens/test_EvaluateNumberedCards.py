from unittest import TestCase, main, skip, SkipTest
from Cards import Card, CardType
from EvaluateNumberedCards import EvaluateNumberedCards

class test_EvaluateNumberedCards(TestCase):

    def test1(self):
        eNC = EvaluateNumberedCards()
        cards = [Card(CardType.NUMBER, i) for i in range(1,4)]
        self.assertTrue(eNC.play(cards))

    def test2(self):
        eNC = EvaluateNumberedCards()
        cards = [Card(CardType.NUMBER, i) for i in range(1, 4)]
        cards.append(Card(CardType.NUMBER, 6))
        self.assertTrue(eNC.play(cards))

    def test3(self):
        eNC = EvaluateNumberedCards()
        cards = [Card(CardType.NUMBER, 2), Card(CardType.NUMBER, 2)]
        self.assertTrue(eNC.play(cards))
    
    def test4(self):
        eNC = EvaluateNumberedCards()
        cards = [Card(CardType.NUMBER, 2), Card(CardType.NUMBER, 6)]
        self.assertFalse(eNC.play(cards))

    def test5(self):
        eNC = EvaluateNumberedCards()
        cards = [Card(CardType.NUMBER, 2), Card(CardType.NUMBER, 4), Card(CardType.NUMBER, 7)]
        self.assertFalse(eNC.play(cards))

    


if __name__ == "__main__":
    main(verbosity=2)
