class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        index = 0
        while index < self.tree_size:
            if self.Tree[index] == key:
                return index
            if self.Tree[index] is None:
                return - index
            
            if key < self.Tree[index]:
                index = 2 * index + 1
            elif key > self.Tree[index]:
                index = 2 * index + 2
        return None # не найден
	
    def AddKey(self, key):
        # добавляем ключ в массив
        index = self.FindKeyIndex(key)
        if index is not None and index <= 0:
            self.Tree[- index] = key
            return -index
        return -1
        # индекс добавленного/существующего ключа или -1 если не удалось