from unittest import TestCase, main, skip, SkipTest
from DrawingAndTrashPile import DrawingAndTrashPile
from Cards import Card, CardType

class test_DrawingAndTrashPile(TestCase):

    def test_init(self):
        piles = DrawingAndTrashPile(toBeShuffled=False)
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
        self.assertEqual(toBeDiscarded, piles._trashPile)
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
        self.assertEqual(2, len(piles._trashPile))
        self.assertEqual(toBeDiscarded, piles._trashPile)
        self.assertEqual(toBeDiscarded, piles.getCardsDiscardedThisTurn())
        self.assertEqual(5, len(hand))
        piles.newTurn()
        self.assertEqual(0, len(piles.getCardsDiscardedThisTurn()))
    
    def test_drawingFromEmpty(self):
        piles = DrawingAndTrashPile()
        hand = [piles._drawingPile.pop(0) for i in range(5)]
        toBeDiscarded = [hand.pop(0), hand.pop(0)]
        piles._trashPile = list(piles._drawingPile)
        piles._drawingPile.clear()
        self.assertEqual(0, len(piles._drawingPile))
        drawn = piles.discardAndDraw(toBeDiscarded)
        for c in drawn:
            hand.append(c)
        self.assertEqual(5, len(hand))
        self.assertEqual(57, len(piles._drawingPile))
        self.assertEqual(0, len(piles._trashPile))
    
    def test_drawingOtherMethod(self):
        piles = DrawingAndTrashPile(otherReloadMethod=True)
        hand = [piles._drawingPile.pop(0) for i in range(5)]
        toBeDiscarded = [hand.pop(0), hand.pop(0)]
        piles._trashPile = list(piles._drawingPile) 
        piles._drawingPile.clear()
        piles._drawingPile.append(piles._trashPile.pop(0))
        self.assertEqual(1, len(piles._drawingPile))
        drawn = piles.discardAndDraw(toBeDiscarded)
        for c in drawn:
            hand.append(c)
        self.assertEqual(5, len(hand))
        self.assertEqual(57, len(piles._drawingPile))
        self.assertEqual(0, len(piles._trashPile))




        
    
if __name__ == "__main__":
    main(verbosity=2)

