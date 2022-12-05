from unittest import TestCase, main, skip, SkipTest
from Hand import Hand
from DrawingAndTrashPile import DrawingAndTrashPile
from Cards import Card, CardType

class test_Hand(TestCase):

    def test_init(self):
        dP = DrawingAndTrashPile(toBeShuffled=False)
        hand = Hand(playerIdx= 1, drawing= dP)
        for i in range(1,6):
            hand._hand[i] = Card(CardType.NUMBER, i)
        self.assertEqual(1, hand.playerIdx)
        self.assertEqual(5, len(hand._hand.keys()))

    
    def test_pickCards(self):
        dP = DrawingAndTrashPile(toBeShuffled=False)
        hand = Hand(playerIdx=1, drawing=dP)
        cards = []
        for i in range(1, 6):
            card = Card(CardType.NUMBER, i)
            hand._hand[i] = card
            cards.append(card)
        
        pickedCards = hand.pickCards([1, 2, 3])
        self.assertEqual(cards[:3], pickedCards)
    

    def test_removePickedCardsAndRedraw(self):
        dP = DrawingAndTrashPile(toBeShuffled=False)
        hand = Hand(playerIdx=1, drawing=dP)
        cards = []
        for i in range(1, 6):
            card = Card(CardType.NUMBER, i)
            hand._hand[i] = card
            cards.append(card)

        pickedCards = hand.pickCards([1, 2, 3])
        self.assertEqual(cards[:3], pickedCards)
        hand.removePickedCardsAndRedraw()
        self.assertNotIn(cards[1], hand.getCards())
    
    
    def test_hasCardOfType(self):
        dP = DrawingAndTrashPile(toBeShuffled=False)
        hand = Hand(playerIdx=1, drawing=dP)
        for i in range(1, 6):
            card = Card(CardType.NUMBER, i)
            hand._hand[i] = card
        self.assertTrue(hand.hasCardOfType(CardType.NUMBER))
        self.assertFalse(hand.hasCardOfType(CardType.KING))



if __name__ == "__main__":
    main(verbosity=2)
