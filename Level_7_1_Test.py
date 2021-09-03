import unittest
from Level_7_1 import SimpleTreeNode, SimpleTree

class DefTest(unittest.TestCase):

    def setUp(self):
        self.Node1 = SimpleTreeNode(10, None)
        self.Node2 = SimpleTreeNode(20, None)
        self.Node3 = SimpleTreeNode(30, None)
        self.Node4 = SimpleTreeNode(40, None)
        self.Node5 = SimpleTreeNode(50, None)
        self.Node6 = SimpleTreeNode(60, None)
        self.Node7 = SimpleTreeNode(70, None)
        self.Node8 = SimpleTreeNode(80, None)
        self.Node9 = SimpleTreeNode(90, None)
        self.Node10 = SimpleTreeNode(10, None)
        self.Node11 = SimpleTreeNode(110, None)

        self.my_tree = SimpleTree(self.Node1)
        self.my_tree.AddChild(self.Node1, self.Node2)
        self.my_tree.AddChild(self.Node1, self.Node3)
        self.my_tree.AddChild(self.Node1, self.Node4)

        self.my_tree.AddChild(self.Node3, self.Node5)
        self.my_tree.AddChild(self.Node3, self.Node6)

        self.my_tree.AddChild(self.Node4, self.Node7)

        self.my_tree.AddChild(self.Node7, self.Node8)
        self.my_tree.AddChild(self.Node7, self.Node9)
        self.my_tree.AddChild(self.Node7, self.Node10)

        self.my_tree.AddChild(self.Node8, self.Node11)

    def test_AddChild(self):
        Node12 = SimpleTreeNode(120, None)
        self.my_tree.AddChild(self.Node5, Node12)
        self.assertIn(Node12, self.Node5.Children)
        self.assertEqual(self.Node5, Node12.Parent)
    
    def test_DeleteNode(self):
        self.my_tree.DeleteNode(self.Node7)
        self.assertNotIn(self.Node7, self.my_tree.GetAllNodes())
        self.assertNotIn(self.Node8, self.my_tree.GetAllNodes())
        self.assertNotIn(self.Node11, self.my_tree.GetAllNodes())

    def test_FindNodesByValue(self):
        Notes_list = self.my_tree.FindNodesByValue(15)
        self.assertEqual([], Notes_list)

        Notes_list1 = self.my_tree.FindNodesByValue(50)
        self.assertIn(self.Node5, Notes_list1)

        Notes_list2 = self.my_tree.FindNodesByValue(50)
        self.assertIn(self.Node5, Notes_list1)

        Notes_list3 = self.my_tree.FindNodesByValue(10)
        self.assertIn(self.Node1, Notes_list3)
        self.assertIn(self.Node10, Notes_list3)

    def test_MoveNode(self):
        self.my_tree.MoveNode(self.Node7, self.Node2)
        self.assertEqual([self.Node7], self.Node2.Children)
        self.assertEqual(self.Node7.Parent, self.Node2)
        self.assertEqual([], self.Node4.Children)

    def tect_Count(self):
        self.assertEqual(self.my_tree.Count(), 11)

    def twst_LeafCount(self):
        self.assertEqual(self.my_tree.LeafCount(), 6)

if __name__ == '__main__':
    unittest.main()