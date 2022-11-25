from unittest import TestCase, main, skip, SkipTest
from DrawingAndTrashPile import DrawingAndTrashPile
from Cards import Card, CardType

class test_DrawingAndTrashPile(TestCase):

    def test_init(self):
        piles = DrawingAndTrashPile()
        self.assertIsInstance(piles._drawingPile[0].type, CardType)
        self.assertEqual(len(piles._drawingPile), 62)
        self.assertEqual(len(piles._trashPile), 0)
        

    def test_cardGeneration(self):
        piles = DrawingAndTrashPile()
        arr = []
        piles.generateCards(arr)
        self.assertIsInstance(arr[-1].value, int)
    
    def test_Discarding(self):
        piles = DrawingAndTrashPile()
        cards = []
        piles.generateCards(cards)
        hand = cards[:5]
        toBeDiscarded = [hand.pop(0)]
        hand.append(piles.discardAndDraw(toBeDiscarded))    
        self.assertEqual(1, len(piles._trashPile))
        self.assertEqual(toBeDiscarded, piles._trashPile[0])
        self.assertEqual(5, len(hand))


if __name__ == "__main__":
    main(verbosity=2)

