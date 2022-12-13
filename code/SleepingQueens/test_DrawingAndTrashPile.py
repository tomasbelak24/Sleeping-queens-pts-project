from unittest import TestCase, main, skip, SkipTest
from DrawingAndTrashPile import DrawingAndTrashPile
from Cards import Card, CardType
from DrawingPileMethods import DrawingPileMethod

class test_DrawingAndTrashPile(TestCase):

    def test_init(self):
        piles = DrawingAndTrashPile(toBeShuffled=False)
        self.assertIsInstance(piles.drawingPile[0].type, CardType)
        self.assertEqual(len(piles.drawingPile), 62)
        self.assertEqual(len(piles.trashPile), 0)
        

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
        self.assertEqual(1, len(piles.trashPile))
        self.assertEqual(toBeDiscarded, piles.trashPile)
        self.assertEqual(toBeDiscarded, piles.getCardsDiscardedThisTurn())
        self.assertEqual(5, len(hand))
        piles.newTurn()
        self.assertEqual(0,len(piles.getCardsDiscardedThisTurn()))
    
    def test_DiscardingTwo(self):
        piles = DrawingAndTrashPile()
        cards = []
        piles.generateCards(cards)
        hand = cards[:5]
        toBeDiscarded = [hand.pop(0), hand.pop(0)]
        drawn = piles.discardAndDraw(toBeDiscarded)
        for c in drawn:
            hand.append(c)
        self.assertEqual(2, len(piles.trashPile))
        self.assertEqual(toBeDiscarded, piles.trashPile)
        self.assertEqual(toBeDiscarded, piles.getCardsDiscardedThisTurn())
        self.assertEqual(5, len(hand))
        piles.newTurn()
        self.assertEqual(0, len(piles.getCardsDiscardedThisTurn()))
    
    def test_drawingFromEmpty(self):
        piles = DrawingAndTrashPile()
        hand = [piles.drawingPile.pop(0) for i in range(5)]
        toBeDiscarded = [hand.pop(0), hand.pop(0)]
        piles.trashPile = list(piles.drawingPile)
        piles.drawingPile.clear()
        self.assertEqual(0, len(piles.drawingPile))
        drawn = piles.discardAndDraw(toBeDiscarded)
        for c in drawn:
            hand.append(c)
        self.assertEqual(5, len(hand))
        self.assertEqual(57, len(piles.drawingPile))
        self.assertEqual(0, len(piles.trashPile))
    
    def test_drawingOtherMethod(self):
        piles = DrawingAndTrashPile(
            toBeShuffled=False, reloadMethod=DrawingPileMethod.drawingPileMethod2)
        hand = [piles.drawingPile.pop(0) for i in range(5)]
        toBeDiscarded = [hand.pop(0), hand.pop(0)]
        piles.trashPile = list(piles.drawingPile) 
        piles.drawingPile.clear()
        piles.drawingPile.append(piles.trashPile.pop(0))
        self.assertEqual(1, len(piles.drawingPile))
        drawn = piles.discardAndDraw(toBeDiscarded)
        for c in drawn:
            hand.append(c)
        self.assertEqual(5, len(hand))
        self.assertEqual(57, len(piles.drawingPile))
        self.assertEqual(0, len(piles.trashPile))


if __name__ == "__main__":
    main(verbosity=2)

