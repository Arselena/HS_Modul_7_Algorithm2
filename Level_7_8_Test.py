import unittest
from Level_7_8 import *

class DefTast(unittest.TestCase):

    def setUp(self):
        self.my_SimpleGrap_0 = SimpleGraph(0)
        self.my_SimpleGrap_1 = SimpleGraph(1)
        self.my_SimpleGrap_9 = SimpleGraph(9)

    def test_0(self):
        self.my_SimpleGrap_0.AddVertex(5)
        self.assertEqual(self.my_SimpleGrap_0.max_vertex, 0)
        self.assertEqual(self.my_SimpleGrap_0.vertex, [])

        self.my_SimpleGrap_0.AddEdge(1, 2)
        self.assertEqual(self.my_SimpleGrap_0.IsEdge(1,2), False)

        self.my_SimpleGrap_0.RemoveVertex(0)
        self.assertEqual(self.my_SimpleGrap_0.vertex, [])

    def test_1(self):
        self.my_SimpleGrap_1.AddVertex(5)
        self.assertEqual(self.my_SimpleGrap_1.max_vertex, 1)
        self.assertEqual(self.my_SimpleGrap_1.vertex[0].Value, 5)

        self.my_SimpleGrap_1.AddEdge(1, 2)
        self.assertEqual(self.my_SimpleGrap_1.IsEdge(1,2), False)

        self.my_SimpleGrap_1.AddEdge(0, 0)
        self.assertEqual(self.my_SimpleGrap_1.IsEdge(0,0), True)

        self.my_SimpleGrap_1.RemoveVertex(0)
        self.assertEqual(self.my_SimpleGrap_1.vertex, [None])
        self.assertEqual(self.my_SimpleGrap_1.IsEdge(0,0), False)

    def test_2(self):
        self.my_SimpleGrap_9.AddVertex(5)
        self.assertEqual(self.my_SimpleGrap_9.max_vertex, 9)
        self.assertEqual(self.my_SimpleGrap_9.vertex[0].Value, 5)
        self.my_SimpleGrap_9.AddVertex(4)
        self.my_SimpleGrap_9.AddVertex(6)
        self.my_SimpleGrap_9.AddVertex(7)
        self.my_SimpleGrap_9.AddVertex(8)
        self.my_SimpleGrap_9.AddVertex(9)
        self.assertEqual(self.my_SimpleGrap_9.vertex[1].Value, 4)
        self.assertEqual(self.my_SimpleGrap_9.vertex[2].Value, 6)
        self.assertEqual(self.my_SimpleGrap_9.vertex[3].Value, 7)
        self.assertEqual(self.my_SimpleGrap_9.vertex[4].Value, 8)
        self.assertEqual(self.my_SimpleGrap_9.vertex[5].Value, 9)
        
        self.my_SimpleGrap_9.AddEdge(1, 2)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(1,2), True)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(2,1), True)

        self.my_SimpleGrap_9.AddEdge(1, 3)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(1,3), True)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(3,1), True)

        self.my_SimpleGrap_9.AddEdge(2, 3)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(2,3), True)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(3,2), True)

        self.assertEqual(self.my_SimpleGrap_9.IsEdge(0,0), False)

        self.my_SimpleGrap_9.RemoveVertex(1)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(1,2), False)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(2,1), False)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(1,3), False)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(3,1), False)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(2,3), True)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(3,2), True)

        self.my_SimpleGrap_9.RemoveEdge(3,2)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(2,3), False)
        self.assertEqual(self.my_SimpleGrap_9.IsEdge(3,2), False)

if __name__ == '__main__':
    unittest.main()