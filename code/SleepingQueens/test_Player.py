from unittest import TestCase, main, skip, SkipTest
from Game import Game
from Cards import Card, CardType

TEST_VAL = 99

class PlayerTest(TestCase):

    def testKral(self):
        game = Game(2)
        game.dealCardsToPlayers()
        self.assertEqual(2, game.numberOfPlayers)
        p1 = game.players[0]
        p2 = game.players[1]
        self.assertEqual(0, len(p1.awokenQueens.collection.keys()))
        self.assertEqual(0, len(p2.awokenQueens.collection.keys()))
        p1.play([0], 1)
        self.assertEqual(1, len(p1.awokenQueens.collection.keys()))
        
    def testRytier(self):
        game = Game(2)
        game.dealCardsToPlayers()
        self.assertEqual(2, game.numberOfPlayers)
        p1 = game.players[0]
        p2 = game.players[1]
        p2.playerHand._hand[0] = Card(CardType.KING, TEST_VAL)
        p1.play([0], 1)
        self.assertEqual(1, len(p1.awokenQueens.collection.keys()))
        p2.playerHand._hand[0] = Card(CardType.KNIGHT, TEST_VAL)
        p2.play([0], 0, 0)
        self.assertEqual(0, len(p1.awokenQueens.collection.keys()))
        self.assertEqual(1, len(p2.awokenQueens.collection.keys()))

    def testObranaPredRytierom(self):
        game = Game(2)
        game.dealCardsToPlayers()
        self.assertEqual(2, game.numberOfPlayers)
        p1 = game.players[0]
        p2 = game.players[1]
        p2.playerHand._hand[0] = Card(CardType.KING, TEST_VAL)
        p1.play([0], 1)
        self.assertEqual(1, len(p1.awokenQueens.collection.keys()))
        p2.playerHand._hand[0] = Card(CardType.KNIGHT, TEST_VAL)
        p1.playerHand._hand[0] = Card(CardType.DRAGON, TEST_VAL)
        p2.play([0],0,0)
        # obrana awokenQ pred rytierom
        self.assertEqual(1, len(p1.awokenQueens.collection.keys()))
        
    def testUspatieKralovny(self):
        game = Game(2)
        game.dealCardsToPlayers()
        self.assertEqual(2, game.numberOfPlayers)
        p1 = game.players[0]
        p2 = game.players[1]
        p2.playerHand._hand[0] = Card(CardType.KING, TEST_VAL)
        p1.play([0], 1)
        self.assertEqual(1, len(p1.awokenQueens.collection.keys()))
        #uspatie kralovny
        p2.playerHand._hand[0] = Card(CardType.SLEEPING_POTION, TEST_VAL)
        self.assertEqual(11, len(game.sleepingQueens.collection.keys()))
        p2.play([0],0,0)
        self.assertEqual(12, len(game.sleepingQueens.collection.keys()))

    def testObranaPredUspatimKralovny(self):
        game = Game(2)
        game.dealCardsToPlayers()
        self.assertEqual(2, game.numberOfPlayers)
        p1 = game.players[0]
        p2 = game.players[1]
        self.assertEqual(12, len(game.sleepingQueens.collection.keys()))
        p1.playerHand._hand[0] = Card(CardType.MAGIC_WAND, TEST_VAL)
        p2.playerHand._hand[0] = Card(CardType.SLEEPING_POTION, TEST_VAL)
        self.assertEqual(12, len(game.sleepingQueens.collection.keys()))

    def testNumberedKartySpravne(self):
        game = Game(2)
        self.assertEqual(2, game.numberOfPlayers)
        p1 = game.players[0]
        p2 = game.players[1]
        for i in range(5):
            p1.playerHand._hand[i] = Card(CardType.NUMBER, i+1)
            p2.playerHand._hand[i] = Card(CardType.NUMBER, 2*(i+1))
        handBefore = p1.playerHand._hand.copy()
        self.assertTrue(p1.play([0, 1, 2]))
        handAfter = p1.playerHand._hand.copy()
        self.assertFalse(handBefore == handAfter)

    def testNumberedKartyNeSpravne(self):
        game = Game(2)
        self.assertEqual(2, game.numberOfPlayers)
        p1 = game.players[0]
        p2 = game.players[1]
        for i in range(5):
            p1.playerHand._hand[i] = Card(CardType.NUMBER, i+1)
            p2.playerHand._hand[i] = Card(CardType.NUMBER, 2*(i+1))
        handBefore = p1.playerHand._hand.copy()
        self.assertIsNone(p1.play([0, 1, 4]))
        handAfter = p1.playerHand._hand.copy()
        self.assertTrue(handBefore == handAfter)




    
        

    


if __name__ == "__main__":
    main(verbosity=2)
