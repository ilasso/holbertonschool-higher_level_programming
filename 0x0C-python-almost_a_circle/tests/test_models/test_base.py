#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """ Class: TestBase : to test class Base
               functions must be inic by test_
               test class name could by named anyway
    """
    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        self.assertTrue(len(base.__doc__) > 0)
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.__init__.__doc__) > 0)

    def test_trivial(self):
        """ Function: test_trivial
                      to test trivial cases
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base(-3)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -3)


if __name__ == '__main__':
    unittest.main()
