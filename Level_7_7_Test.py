import unittest
from Level_7_7 import Heap

class DefTest(unittest.TestCase):
    def setUp(self):
        self.my_HeapEmpty = Heap()

        self.my_HeapOne = Heap()
        self.my_HeapOne.MakeHeap([1],0)

        self.my_Heap1 = Heap()
        self.my_Heap1.MakeHeap([1,2,3,4,5,6,7], 2)

        self.my_Heap2 = Heap()
        self.my_Heap2.MakeHeap([7,6,5,4,3,2,1], 3)


    def test_empty(self):
        self.assertEqual(self.my_HeapEmpty.GetMax(), -1)
        self.assertEqual(self.my_HeapEmpty.Add(9), False)

    def test_one(self):
        self.assertEqual(self.my_HeapOne.GetMax(), 1)
        self.assertEqual(self.my_HeapOne.GetMax(), -1)
        self.my_HeapOne.Add(1)
        self.assertEqual(self.my_HeapOne.HeapArray, [1])

    def test_1(self):
        self.assertEqual(self.my_Heap1.HeapArray, [7, 4, 6, 1, 3, 2, 5])
        self.assertEqual(self.my_Heap1.GetMax(), 7)
        self.assertEqual(self.my_Heap1.HeapArray, [6, 4, 5, 1, 3, 2, None])

    def test_2(self):
        self.assertEqual(self.my_Heap2.HeapArray, [7, 6, 5, 4, 3, 2, 1, None, None, None, None, None, None, None, None])
        self.assertEqual(self.my_Heap2.GetMax(), 7)
        self.assertEqual(self.my_Heap2.HeapArray, [6, 1, 5, 4, 3, 2, None, None, None, None, None, None, None, None, None])

if __name__ == '__main__':
    unittest.main()