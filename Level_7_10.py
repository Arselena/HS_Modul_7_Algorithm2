import ctypes

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class Stack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)

    def push(self, item):  # добавить в хвост
        self.stack.append(item)

    def pop(self):
        if self.stack == []:
            return None # если стек пустой, вернуть None
        return self.stack.pop() # вернуть с удалением последний эл-т

    def peek(self):
        if self.stack == []:
            return None # если стек пустой, вернуть None
        return self.stack[-1] # вернуть последний эл-т
    

class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size  # максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)]
        # матрица смежности, где 0 означает отсутствие ребра между i-й вершиной (первое измерение) и j-й вершиной (второе измерение), а 1 означает наличие ребра
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        # ваш код добавления новой вершины 
        # с значением value 
        # в свободное место массива vertex
        new_vertex = Vertex(v)
        for i in range(self.max_vertex):
            if self.vertex[i] == None:
                self.vertex[i] = new_vertex
                return
        pass 
	
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if v < self.max_vertex:
            self.vertex[v] = None
            for j in range(self.max_vertex):
                self.m_adjacency[v][j] = 0
            for i in range(self.max_vertex):
                self.m_adjacency[i][v] = 0
        pass
	
    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if v1 < self.max_vertex and v1 < self.max_vertex:
            if self.m_adjacency[v1][v2] == 1 or self.m_adjacency[v2][v1] == 1:
                return True
        return False
	
    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if v1 < self.max_vertex and v1 < self.max_vertex:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
        pass
	
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if v1 < self.max_vertex and v1 < self.max_vertex:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
        pass

    def DepthFirstSearch(self, VFrom, VTo):
            # узлы задаются позициями в списке vertex
            # возвращается список узлов -- путь из VFrom в VTo
            # или [] если пути нету
        Stak_Hit = Stack()  # делаем стек пустым
        for i in self.vertex: # все вершины графа отмечаем как непосещённые
            i.Hit = False
                
        X_curent = VFrom # Выбираем текущую вершину
        while True:
            self.vertex[X_curent].Hit = True # Фиксируем вершину как посещённую.
            Stak_Hit.push(self.vertex[X_curent]) # Помещаем вершину в стек
            if self.m_adjacency[X_curent][VTo] == 1:
                Stak_Hit.push(self.vertex[VTo])
                return Stak_Hit.stack
            
            V_adjacent = 0
            while V_adjacent < self.max_vertex - 1:
                v_hit = True
                if self.m_adjacency[X_curent][V_adjacent] == 1 and self.vertex[V_adjacent].Hit == False:
                    X_curent = V_adjacent
                    v_hit = False
                    break
                V_adjacent += 1
            if v_hit == True:
                Stak_Hit.pop()
                if Stak_Hit.stack == []:
                    return []
                X_curent = self.vertex.index(Stak_Hit.pop())