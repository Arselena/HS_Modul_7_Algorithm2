class Vertex:

    def __init__(self, val):
        self.Value = val
  
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
