import unittest
from Level_7_4 import aBST

class DefTest(unittest.TestCase):
    def setUp(self):
        self.my_tree = aBST(3)
        self.my_tree_None = aBST(0)

    def test_1(self):
        index1 = self.my_tree.FindKeyIndex(0)
        index50 = self.my_tree.FindKeyIndex(50)
        self.assertEqual(index1, 0)
        self.assertEqual(index50, 0)
        
        index_add1 = self.my_tree_None.AddKey(50)
        index_add2 = self.my_tree_None.AddKey(75)
        self.assertEqual(index_add1, 0)
        self.assertEqual(index_add2, -1)
        
        self.my_tree.AddKey(50)
        index_add75 = self.my_tree.AddKey(75)
        self.assertEqual(index_add75, 2)
        index_add25 = self.my_tree.AddKey(25)
        self.assertEqual(index_add25, 1)

        self.my_tree.AddKey(62)
        self.my_tree.AddKey(37)
        self.my_tree.AddKey(55)
        self.my_tree.AddKey(43)
        self.my_tree.AddKey(31)
        self.my_tree.AddKey(84)
        self.my_tree.AddKey(92)
        self.assertEqual(self.my_tree.Tree, [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])

if __name__ == '__main__':
    unittest.main()