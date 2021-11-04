# 7.1. Деревья
class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            self.Root = NewChild
        else:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)
  
    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is self.Root:
            self.Root = None
        else:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

    @staticmethod
    def tree_traversal(Node, All_Nodes_list, Used_Nodes):
        if Node.Children != []:
            All_Nodes_list.extend(Node.Children)
        for Children in Node.Children:
            if Children not in Used_Nodes:
                Used_Nodes.append(Children)
                SimpleTree.tree_traversal(Children, All_Nodes_list, Used_Nodes)
        return All_Nodes_list

    def GetAllNodes(self):
        if self.Root is not None:
            return SimpleTree.tree_traversal(self.Root, [self.Root], [self.Root])
        return None

    def FindNodesByValue(self, val):
        NodesByValue = []
        if self.Root is not None:
            All_Nodes_list = SimpleTree.tree_traversal(self.Root, [self.Root], [self.Root])
            for Node in All_Nodes_list:
                if Node.NodeValue == val:
                    NodesByValue.append(Node)
        return NodesByValue
   
    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)
   
    def Count(self, curent_root): # количество всех узлов в дереве
        All_Nodes_list = SimpleTree.tree_traversal(curent_root, [curent_root], [curent_root])
        return len(All_Nodes_list)

    def LeafCount(self): # количество листьев в дереве
        All_Nodes_list = SimpleTree.tree_traversal(self.Root, [self.Root], [self.Root])
        Leaf_Count_int = 0
        for Node in All_Nodes_list:
            if Node.Children == []:
                Leaf_Count_int += 1
        return Leaf_Count_int

    #  Мметод, который перебирает всё дерево и прописывает каждому узлу его уровень.
    @staticmethod
    def tree_traversal_with_level(Node, All_Nodes_dict, Used_Nodes, level=0):
        level += 1
        if Node.Children != []:
            for Children in Node.Children:
                All_Nodes_dict[Children] = level
        
        for Children in Node.Children:
            if Children not in Used_Nodes:
                Used_Nodes.append(Children)
                SimpleTree.tree_traversal_with_level(Children, All_Nodes_dict, Used_Nodes, level)
        return All_Nodes_dict

    def GetAllNodes_with_level(self):
        if self.Root is not None:
            return SimpleTree.tree_traversal_with_level(self.Root, {self.Root:0}, [self.Root])
        return None

    def GetLeafs(self):
        All_Nodes_list = SimpleTree.tree_traversal(self.Root, [self.Root], [self.Root])
        lifs = []
        for Node in All_Nodes_list:
            if Node.Children == []:
                lifs.append(Node)
        return lifs

    def EvenTrees(self):
        if self.Count(self.Root) % 2 != 0:
            return None

        lifs = self.GetLeafs()
        node_connection = []
        for i in range(len(lifs)):
            node = lifs[i]
            while node.Parent != self.Root:
                if self.Count(node.Parent) % 2 == 0 and node.Parent not in node_connection:
                    node_connection.append(node.Parent.Parent)
                    node_connection.append(node.Parent)
                node = node.Parent
        return node_connection