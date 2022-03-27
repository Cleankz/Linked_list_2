import unittest
import random
from Link_2 import Node
from Link_2 import LinkedList2

class MyTests(unittest.TestCase):
    def test_add_in_tail(self):
        test_link = LinkedList2()
        for i in range(100000):
            test_link.add_in_tail(Node(random.randint(0,100000)))
    def test_find(self):
        test_link = LinkedList2()
        for i in range(100):
            test_link.add_in_tail(Node(random.randint(0,100)))
        for i in range(100):
            test_link.find(random.randint(0,100))
    def test_find_all(self):
        test_link = LinkedList2()
        for i in range(100):
            test_link.add_in_tail(Node(random.randint(0,100)))
        for i in range(100):
            test_link.find_all(random.randint(0,100))
    def test_delete(self):
        test_link = LinkedList2()
        self.assertEqual(test_link.delete(10),None)
        test_link.add_in_tail(Node(10))
        self.assertEqual(test_link.delete(10),None)
        test_link.add_in_tail(Node(10))
        test_link.add_in_tail(Node(11))
        self.assertEqual(test_link.delete(10),None)
        test_link.add_in_tail(Node(12))
        self.assertEqual(test_link.delete(12),None)
        test_link_2 = LinkedList2()
        test_link_2.add_in_tail(Node(12))
        test_link_2.add_in_tail(Node(12))
        test_link_2.add_in_tail(Node(12))
        test_link_2.add_in_tail(Node(12))
        test_link_2.delete(12,all =True)
        for i in range(10000):
            test_link.add_in_tail(Node(random.randint(0,10000)))
        for j in range(10000):
            test_link.delete(random.randint(0,10000))
        for i in range(10000):
            test_link.add_in_tail(Node(random.randint(0,10000)))
        for j in range(10000):
            test_link.delete(random.randint(0,j),all=True)
    def test_clean(self):
        test_link = LinkedList2()
        for i in range(100000):
            test_link.add_in_tail(Node(random.randint(0,1000)))
        test_link.clean()
        self.assertEqual(test_link.len(),0)
    def test_len(self):
        test_link = LinkedList2()
        self.assertEqual(test_link.len(),0)
        for i in range(100000):
            test_link.add_in_tail(Node(random.randint(0,1000)))
        self.assertEqual(test_link.len(),100000)
    def test_insert(sef):
        test_link = LinkedList2()
        n = Node(13)
        test_link.insert(None,Node(12))
        test_link.insert(None,n)
        test_link.insert(n,Node(15))
        for i in range(10000):
            test_link.insert(None,Node(random.randint(0,10000)))

    def test_add_in_head(self):
        test_link = LinkedList2()
        for i in range(100000):
            test_link.add_in_head(Node(random.randint(0,100000)))


if __name__ == '__main__':
    unittest.main()

