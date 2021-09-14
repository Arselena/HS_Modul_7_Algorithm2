import unittest
from Level_7_2_2 import BSTNode, BSTFind, BST

class DefTest(unittest.TestCase):

    def setUp(self):
        self.Node_8 = BSTNode(8, 1, None)
        self.Node_4 = BSTNode(4, 2, self.Node_8)
        self.Node_12 = BSTNode(12, 3, self.Node_8)
        self.Node_2 = BSTNode(2, 4, self.Node_4)
        self.Node_6 = BSTNode(6, 5, self.Node_4)
        self.Node_10 = BSTNode(10, 6, self.Node_12)
        self.Node_14 = BSTNode(14, 7, self.Node_12)

        self.Node_1 = BSTNode(1, 1, self.Node_2)
        self.Node_3 = BSTNode(3, 2, self.Node_2)
        self.Node_5 = BSTNode(5, 3, self.Node_6)
        self.Node_7 = BSTNode(7, 4, self.Node_6)
        self.Node_9 = BSTNode(9, 5, self.Node_10)
        self.Node_11 = BSTNode(11, 6, self.Node_10)
        self.Node_13 = BSTNode(13, 7, self.Node_14)
        self.Node_15 = BSTNode(15, 7, self.Node_14)

        self.Node_8.LeftChild = self.Node_4
        self.Node_8.RightChild = self.Node_12
        self.Node_4.LeftChild = self.Node_2
        self.Node_4.RightChild = self.Node_6
        self.Node_12.LeftChild = self.Node_10
        self.Node_12.RightChild = self.Node_14

        self.Node_2.LeftChild = self.Node_1
        self.Node_2.RightChild = self.Node_3
        self.Node_6.LeftChild = self.Node_5
        self.Node_6.RightChild = self.Node_7
        self.Node_10.LeftChild = self.Node_9
        self.Node_10.RightChild = self.Node_11
        self.Node_14.LeftChild = self.Node_13
        self.Node_14.RightChild = self.Node_15

        self.my_tree = BST(self.Node_8)

    def test_FindNodeByKey(self):
        test_BSTFind_0 = self.my_tree.FindNodeByKey(0)
        test_BSTFind_16 = self.my_tree.FindNodeByKey(16)
        test_BSTFind_Root = self.my_tree.FindNodeByKey(8)
        test_BSTFind_6 = self.my_tree.FindNodeByKey(6)

        # Ключ не существует, добавление к Node_1, левый потомок
        self.assertEqual(test_BSTFind_0.NodeHasKey, False)
        self.assertEqual(test_BSTFind_0.ToLeft, True)
        self.assertEqual(test_BSTFind_0.Node, self.Node_1)

        # Ключ не существует, добавление к Node_15, правый потомок
        self.assertEqual(test_BSTFind_16.NodeHasKey, False)
        self.assertEqual(test_BSTFind_16.ToLeft, False)
        self.assertEqual(test_BSTFind_16.Node, self.Node_15)

        # Ключ существует и является корнем
        self.assertEqual(test_BSTFind_Root.NodeHasKey, True)
        self.assertEqual(test_BSTFind_Root.ToLeft, False)
        self.assertEqual(test_BSTFind_Root.Node, self.Node_8)
    
        # Ключ существует
        self.assertEqual(test_BSTFind_6.NodeHasKey, True)
        self.assertEqual(test_BSTFind_6.ToLeft, False)
        self.assertEqual(test_BSTFind_6.Node, self.Node_6)

    def test_AddKeyValue(self):
        # удаляем Узел_6, тогда вместо Узел_6 встанет Узел_7 (с потомком Узел_5)
        self.my_tree.DeleteNodeByKey(6)
        test_BSTFind_Del_6 = self.my_tree.FindNodeByKey(6)
        self.assertEqual(test_BSTFind_Del_6.NodeHasKey, False)
        
        # Добавляем узел правым потомком
        self.my_tree.AddKeyValue(6, 66)
        test_BSTFind_Add_6 = self.my_tree.FindNodeByKey(6)
        self.assertEqual(test_BSTFind_Add_6.NodeHasKey, True)
        self.assertEqual(test_BSTFind_Add_6.Node.NodeValue, 66)
        self.assertEqual(test_BSTFind_Add_6.Node.Parent.NodeKey, 5) # Родителем Узел_6 будет Узел_5
        self.assertEqual(self.Node_5.RightChild, test_BSTFind_Add_6.Node) # Правым потомком Узел_5 будет Узел_6
        
        # добавляем узел левым потомком
        self.assertEqual(self.my_tree.FindNodeByKey(0).NodeHasKey, False) # проверили, что в дереве нет узла с этим ключом
        self.my_tree.AddKeyValue(0, 0)
        test_BSTFind_Add_0 = self.my_tree.FindNodeByKey(0)
        self.assertEqual(test_BSTFind_Add_0.NodeHasKey, True)
        self.assertEqual(test_BSTFind_Add_0.Node.NodeValue, 0)
        self.assertEqual(test_BSTFind_Add_0.Node.Parent.NodeKey, 1) # Родителем Узел_0 будет Узел_1
        self.assertEqual(self.Node_1.LeftChild, test_BSTFind_Add_0.Node) # Левым потомком Узел_1 будет Узел_0

        # попытка добавить узел, который уже есть в дереве
        self.assertEqual(self.my_tree.FindNodeByKey(8).NodeHasKey, True) # проверили, что в дереве есть узел с этим ключом 
        self.my_tree.AddKeyValue(8, 0)
        test_BSTFind_Add_8 = self.my_tree.FindNodeByKey(8)
        self.assertEqual(test_BSTFind_Add_8.NodeHasKey, True)
        self.assertEqual(test_BSTFind_Add_8.Node.LeftChild, self.Node_4)
        self.assertEqual(test_BSTFind_Add_8.Node.RightChild, self.Node_12)
        self.assertEqual(self.Node_8, self.my_tree.Root)
        
    def test_FinMinMax(self):
        min_root = self.my_tree.FinMinMax(None, False)
        max_root = self.my_tree.FinMinMax(None, True)
        self.assertEqual(min_root, self.Node_1)
        self.assertEqual(max_root, self.Node_15)

        min_Node_4 = self.my_tree.FinMinMax(self.Node_4, False)
        max_Node_4 = self.my_tree.FinMinMax(self.Node_4, True)
        self.assertEqual(min_Node_4, self.Node_1)
        self.assertEqual(max_Node_4, self.Node_7)

        min_Node_11 = self.my_tree.FinMinMax(self.Node_11, False)
        max_Node_11 = self.my_tree.FinMinMax(self.Node_11, True)
        self.assertEqual(min_Node_11, max_Node_11)

    def test_DeleteNodeByKey(self):
        # Удаляем корень
        del_Root = self.my_tree.DeleteNodeByKey(8)
        self.assertEqual(self.my_tree.Root, self.Node_9)
        self.assertEqual(self.Node_9.LeftChild, self.Node_4)
        self.assertEqual(self.Node_9.RightChild, self.Node_12)
        self.assertEqual(self.Node_4.Parent, self.Node_9)
        self.assertEqual(self.Node_12.Parent, self.Node_9)

if __name__ == '__main__':
    unittest.main()