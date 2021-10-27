class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
		
    def MakeHeap(self, a, depth): # создаём массив кучи HeapArray из заданного, размер массива выбираем на основе глубины depth 
        self.Size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * self.Size
        for i in a:
            self.Add(i)
        pass

    def FindNoneId(self):
        if self.HeapArray != []:
            for i in range(self.Size):
                if self.HeapArray[i] == None:
                    return i
        return False

    def GetMax(self):   # вернуть значение корня и перестроить кучу
        def max_child_index(index):
            left = index * 2 + 1
            right = index * 2 + 2
            if self.HeapArray[right] and self.HeapArray[right] > self.HeapArray[left]: 
                return right
            return left
        
        if self.HeapArray == [] or self.HeapArray[0] is None:
            return -1   # return -1 # если куча пуста
      
        max_node = self.HeapArray[0]
        if self.Size == 1:
            self.HeapArray[0] = None
            return max_node

        NoneId = self.FindNoneId()
        if NoneId is False:
            NoneId = self.Size
        
        self.HeapArray[0] = self.HeapArray[NoneId - 1]
        self.HeapArray[NoneId - 1] = None

        child_index = max_child_index(0)
        i = 0
        while child_index and self.HeapArray[i] < self.HeapArray[child_index]:
            self.HeapArray[i], self.HeapArray[child_index] = self.HeapArray[child_index], self.HeapArray[i]
            i = child_index
            if child_index < int((self.Size - 1) / 2) and self.HeapArray[int((self.Size - 1) / 2)]:
                child_index = max_child_index(i)
            else:
                child_index = 0
        
        return max_node

    def Add(self, key): # добавляем новый элемент key в кучу и перестраиваем её
        curent_node = self.FindNoneId()
        if curent_node is not False:
            self.HeapArray[curent_node] = key
            if curent_node == 0:
                return
            parent_node = int((curent_node - 1) / 2)
            while self.HeapArray[curent_node] > self.HeapArray[parent_node] and curent_node != 0:
                self.HeapArray[curent_node], self.HeapArray[parent_node] = self.HeapArray[parent_node], self.HeapArray[curent_node]
                curent_node = parent_node
                parent_node = int((curent_node - 1) / 2)
        return False # если куча вся заполнена

my_Heap1 = Heap()
# my_Heap1.MakeHeap([], 3)
# print(my_Heap1.HeapArray)
my_Heap1.Add(9)
print(my_Heap1.HeapArray)
