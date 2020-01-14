#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    "unittest max_integer"

    def test_isThereDoc(self):
        """Documentation test cases"""
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_TrivialCases(self):
        """Trivial test cases"""
        self.assertEqual(max_integer([100, 90, 200, 5000, 20, 10]), 5000)
        self.assertEqual(max_integer([100, 100, 100, 100, 100, 100]), 100)
        self.assertEqual(max_integer([100]), 100)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer([-1, -1000, 0]), 0)
        self.assertEqual(max_integer([3, 4.5, 0.5, -1.5, 2.8945, 3.1416]), 4.5)
        self.assertEqual(max_integer([[1, 3, 2], [4, 6], [7, 9]]), [7, 9])
        self.assertEqual(max_integer(['a', 'b']), 'b')
        self.assertEqual(max_integer((1, 5, -3, 7)), 7)
        self.assertEqual(max_integer("Julien"), "u")

    def test_RaiseError(self):
        """ Exeptions test cases"""
        with self.assertRaises(TypeError):
            max_integer(['a', 5])
        with self.assertRaises(TypeError):
            max_integer([10, 3, [4, 5, 6], 7, 8])
        with self.assertRaises(TypeError):
            max_integer(23)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer({1, 5, -3, 7})

if __name__ == '__main__':
    unittest.main()
