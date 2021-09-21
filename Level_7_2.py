# 7.1. Двоичные деревья поиска 
from logging import root


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
        FindNode = FromNode if FromNode is not None else self.Root
        if FindMax is False:
            while FindNode.LeftChild is not None:
                FindNode = FindNode.LeftChild
        else:
            while FindNode.RightChild is not None:
                FindNode = FindNode.RightChild
        return FindNode
	
    def DeleteNodeByKey(self, key):
        def __del_DeleteNode(DeleteNode):
            DeleteNode.Parent = None 
            DeleteNode.LeftChild = None 
            DeleteNode.RightChild = None 
        
        def Move_Node(DeleteNode, MoveNode):
            # определяем связь с родителем 
            if DeleteNode is self.Root:
                MoveNode.Parent = None
                self.Root = MoveNode
            else:
                MoveNode.Parent = DeleteNode.Parent 
                if DeleteNode.Parent.LeftChild == DeleteNode:
                    DeleteNode.Parent.LeftChild = MoveNode
                else:
                    DeleteNode.Parent.RightChild == DeleteNode
                    DeleteNode.Parent.RightChild = MoveNode
            # если у удаляемого узла только левый потомок
            if DeleteNode.LeftChild == MoveNode: 
                return
            # определяем связь с левым потомком удаляемого узла
            if DeleteNode.LeftChild is not None:
                MoveNode.LeftChild = DeleteNode.LeftChild
                DeleteNode.LeftChild.Parent = MoveNode

            # определяем связь с правым потомком удаляемого узла
            if DeleteNode.RightChild != MoveNode: 
                MoveNode.RightChild = DeleteNode.RightChild
                DeleteNode.RightChild.Parent = MoveNode


        DeleteNode_BSTFind = self.FindNodeByKey(key)
        if DeleteNode_BSTFind.NodeHasKey is False: # если узел не найден
            return False
        
        DeleteNode = DeleteNode_BSTFind.Node
        
        # Если в дереве только корень
        if DeleteNode == self.Root and DeleteNode.LeftChild is None and DeleteNode.RightChild is None:
            __del_DeleteNode(DeleteNode)
            self.Root = None
            return True

        # Если удаляемый узел ЛИСТ
        if DeleteNode.LeftChild is None and DeleteNode.RightChild is None:
            if DeleteNode.Parent.LeftChild == DeleteNode:
                DeleteNode.Parent.LeftChild = None
            else:
                DeleteNode.Parent.RightChild = None
            __del_DeleteNode(DeleteNode)
            return True
    
        if DeleteNode.RightChild is None:
            Move_Node(DeleteNode, DeleteNode.LeftChild)
        elif DeleteNode.RightChild.LeftChild is None: # если у правого потомка удаляемого узла нет левого потомка
            Move_Node(DeleteNode, DeleteNode.RightChild)
        else:
            MinNodeOfRightChild = self.FinMinMax(DeleteNode.RightChild, False)
            if MinNodeOfRightChild.RightChild is not None:
                MinNodeOfRightChild.Parent.LeftChild = MinNodeOfRightChild.RightChild
                MinNodeOfRightChild.RightChild.Parent = MinNodeOfRightChild.Parent
            elif DeleteNode.RightChild != MinNodeOfRightChild:
                MinNodeOfRightChild.Parent.LeftChild = None
            Move_Node(DeleteNode, MinNodeOfRightChild)
        
        __del_DeleteNode(DeleteNode)
        return True 

    def Count(self):
        if self.Root == None:
            return 0
        All_Nodes_list = BST.tree_traversal(self.Root, [self.Root], [self.Root])
        return len(All_Nodes_list) # количество узлов в дереве