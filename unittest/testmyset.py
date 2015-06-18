__author__ = 'cwong_000'

import unittest
import myset

class TestMySet(unittest.TestCase):

    def setUp(self):
        self.items = [1, 2, 3, 4]
        self.myset = myset.MySet(self.items)

    def testadditem(self):
        self.items.append(5)
        self.myset.additem(5)
        self.assertEqual(self.myset.set, self.items)

    def testremoveitem(self):
        self.items.remove(5)
        self.myset.removeitem(5)
        self.assertEqual(self.items, self.myset.set)

    def testisempty(self):
        self.assertFalse(self.myset.isempty())
        self.myset.set = []
        self.assertTrue(self.myset.isempty())

    def testhasitem(self):
        self.assertTrue(self.myset.hasitem(2))
        self.assertFalse(self.myset.hasitem("BIT"))

    def testintersection(self):
        testintersect = [1, 2, 3, 4]
        self.assertEqual(self.myset.intersection(self.items), testintersect)

    def testunion(self):
        testunion = [1, 2, 3, 4, 5, 6, 7]
        testinput = [6, 7]
        self.assertEqual(self.myset.union(testinput), testunion)

    def testissubset(self):
        testsubset = [1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(self.myset.issubsetof(testsubset))
        self.assertFalse(self.myset.issubsetof(["NOT", "A", "SUBSET"]))

    def testisequalto(self):
        testequalset = [1, 2, 3, 4]
        self.assertTrue(self.myset.is_equal_to(testequalset))
        self.assertFalse(self.myset.is_equal_to([8, 3, "NO", 5, "Hi"]))

if __name__ == '__main__':
    unittest.main()
