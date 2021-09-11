# 7.1. Двоичные деревья поиска 
class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST: # BinarySearchTree

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    @staticmethod
    def tree_traversal(Node, All_Nodes_list, Used_Nodes):
        if Node.RightChild:
            All_Nodes_list.append(Node.RightChild)
        if Node.LeftChild:
            All_Nodes_list.append(Node.LeftChild)

        for Children in All_Nodes_list:
            if Children not in Used_Nodes:
                Used_Nodes.append(Children)
                BST.tree_traversal(Children, All_Nodes_list, Used_Nodes)
        return All_Nodes_list

    @staticmethod
    def FindByKey(NodeCurrent, key):
        if key == NodeCurrent.Node.NodeKey:
            NodeCurrent.NodeHasKey = True
            return NodeCurrent
        
        if key < NodeCurrent.Node.NodeKey and NodeCurrent.Node.LeftChild is not None:
            NodeCurrent.Node = NodeCurrent.Node.LeftChild
            BST.FindByKey(NodeCurrent, key)
        elif key > NodeCurrent.Node.NodeKey and NodeCurrent.Node.RightChild is not None:
            NodeCurrent.Node = NodeCurrent.Node.RightChild
            BST.FindByKey(NodeCurrent, key)

        if key < NodeCurrent.Node.NodeKey:
            NodeCurrent.ToLeft = True
        return NodeCurrent

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        NodeCurrent = BSTFind()
        NodeCurrent.Node = self.Root
        return BST.FindByKey(NodeCurrent, key)# возвращает BSTFind

    def AddKeyValue(self, key, val):
        NewNode = BSTNode(key, val, None)
        NodeToAdd = self.FindNodeByKey(key)
        if NodeToAdd.NodeHasKey == False:
            NewNode.Parent = NodeToAdd.Node
            if NodeToAdd.ToLeft == True:
                NodeToAdd.Node.LeftChild = NewNode
            else:
                NodeToAdd.Node.RightChild = NewNode
            return True
        # добавляем ключ-значение в дерево
        return False # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        FindNode = FromNode
        if FindMax is False:
            while FindNode.LeftChild is not None:
                FindNode = FindNode.LeftChild
        else:
            while FindNode.RightChild is not None:
                FindNode = FindNode.RightChild
        return FindNode
	
    @staticmethod
    def MoveLeaf(DeleteNode, MoveNode): 
        if DeleteNode.NodeKey > DeleteNode.Parent.NodeKey:
            DeleteNode.Parent.RightChild = MoveNode
        else:
            DeleteNode.Parent.LeftChild = MoveNode

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        DeleteNode_BSTFind = self.FindNodeByKey(key)
        if DeleteNode_BSTFind.NodeHasKey == False: # если узел не найден
            return False 
        DeleteNode = DeleteNode_BSTFind.Node

        if DeleteNode.RightChild is None and DeleteNode.RightChild is None: # если у удаляемого узпа нет потомков
            if DeleteNode is not self.Root:
                BST.MoveLeaf(DeleteNode, None)
            else:
                self.__init__(self, None)
    
        elif DeleteNode.RightChild is None: # если у удаляемого узла нет правого потомка
            if DeleteNode is not self.Root:
                DeleteNode.LeftChild.Parent = DeleteNode.Parent
                BST.MoveLeaf(DeleteNode, DeleteNode.LeftChild)
            else:
                BST.__init__(self, DeleteNode.LeftChild)
        
        elif DeleteNode.LeftChild is None and DeleteNode is self.Root: # если у удаляемого узла нет левого потомка и удаляемый узел = это корень
            BST.__init__(self, DeleteNode.RightChild)

        elif DeleteNode.RightChild.LeftChild is None: # если у удаляемого узла у правтого потомка нет левого потомка
            if DeleteNode is not self.Root:
                DeleteNode.RightChild.Parent = DeleteNode.Parent
                BST.MoveLeaf(DeleteNode, DeleteNode.RightChild)
            else:
                BST.__init__(self, DeleteNode.RightChild)
                self.Root.LeftChild = DeleteNode.LeftChild

        else:
            MinNodeOfRightChild = self.FinMinMax(DeleteNode.RightChild, False)
            if MinNodeOfRightChild.RightChild is not None: # если у правого потомка минимальный узел - не лист
                MinNodeOfRightChild.RightChild.Parent = MinNodeOfRightChild.Parent
                MinNodeOfRightChild.Parent.LeftChild = MinNodeOfRightChild.RightChild
            if DeleteNode is not self.Root:
                BST.MoveLeaf(DeleteNode, MinNodeOfRightChild)
                MinNodeOfRightChild.LeftChild = DeleteNode.LeftChild 
                MinNodeOfRightChild.RightChild = DeleteNode.RightChild 
            else:
                BST.__init__(self, MinNodeOfRightChild)
                self.Root.LeftChild = DeleteNode.LeftChild
                self.Root.RightChild = DeleteNode.RightChild

        DeleteNode.Parent = None 
        DeleteNode.LeftChild = None 
        DeleteNode.RightChild = None 
        return True 

    def Count(self):
        All_Nodes_list = BST.tree_traversal(self.Root, [self.Root], [self.Root])
        return len(All_Nodes_list) # количество узлов в дереве