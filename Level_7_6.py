class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева

    def GenerateTree(self, a):
        def Add_Key_rec(BBST, a_sort, indexs, pred=None, level=0):
            indexs_len = len(indexs)
            if indexs_len == 0:
                return
            centr = indexs[0] + indexs_len // 2
            Node = BSTNode(a_sort[centr], pred)
            BBST.append(Node)
            if pred is None:
                self.Root = Node
            elif pred.NodeKey > Node.NodeKey:
                pred.LeftChild = Node
                Node.Level = level + 1
            else: 
                pred.RightChild = Node
                Node.Level = level + 1
            Add_Key_rec(BBST, a_sort, range(indexs[0], centr), Node, Node.Level)
            Add_Key_rec(BBST, a_sort, range(centr + 1, (indexs[0] + indexs_len)), Node, Node.Level)

        a_sort = sorted(a)
        BBST = []
        Add_Key_rec(BBST, a_sort, range(0, len(a_sort)))
        return BBST

    def IsBalanced(self, root_node):
        def depth(root_node):
            current_depth = 0

            if root_node.LeftChild:
                current_depth = max(current_depth,  depth(root_node.LeftChild))

            if root_node.RightChild:
                current_depth = max(current_depth,  depth(root_node.RightChild))

            return current_depth + 1
        balanse = True
        left_depth = 0
        right_depth = 0
        if root_node.LeftChild:
            self.IsBalanced(root_node.LeftChild)
            left_depth = depth(root_node.LeftChild)
        if root_node.RightChild:
            self.IsBalanced(root_node.RightChild)
            right_depth = depth(root_node.RightChild)
        
        if left_depth == right_depth or left_depth + 1 == right_depth or left_depth == right_depth + 1:
            pass
        else:
            balanse = False
        return balanse