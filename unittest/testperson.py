__author__ = 'cwong_000'

import unittest
import person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = person.Person("Homer", "Simpson")
        self.person.age = 45

    def testconstructor(self):
        self.assertIsInstance(self.person, person.Person)
        self.assertEqual(self.person.firstname, "Homer")
        self.assertEqual(self.person.lastname, "Simpson")

    def testchangename(self):
        self.person.changename("Nelson", "Muntz")
        self.assertEqual(self.person.firstname, "Nelson")
        self.assertEqual(self.person.lastname, "Muntz")

    def testincrement_age(self):
        newage = self.person.age + 1
        self.assertEqual(self.person.incrementage(), newage)

    def testkill(self):
        self.assertTrue(self.person.kill())

if __name__ == '__main__':
    unittest.main()