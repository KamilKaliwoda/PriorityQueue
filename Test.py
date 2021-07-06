import unittest
from PriorityQueue import Queue


class MyTestCase(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        priority = [4, 7, 2, 5, 7, 6, 2, 1]
        data = ["A", "L", "G", "O", "R", "Y", "T", "M"]
        for index in range(8):
            q.enqueue(priority[index], data[index])
        self.assertEqual(str(q), '[7: L, 7: R, 6: Y, 4: A, 5: O, 2: G, 2: T, 1: M]')
        self.assertEqual(q.dequeue(), 'L')
        self.assertEqual(str(q), '[7: R, 5: O, 6: Y, 4: A, 1: M, 2: G, 2: T]')
        self.assertEqual(q.peek(), 'R')
        while not q.is_empty():
            q.dequeue()
        self.assertEqual(str(q), '[]')


if __name__ == '__main__':
    unittest.main()
