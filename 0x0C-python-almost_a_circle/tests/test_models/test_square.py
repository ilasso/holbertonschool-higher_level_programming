#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle
from models import square
from models.square import Square
import sys
from io import StringIO


class TestSquare(unittest.TestCase):
    """ Class: TestSquare: to test class Square
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        Base._Base__nb_objects = 0
        self.assertTrue(len(square.__doc__) > 0)
        self.assertTrue(len(Square.__doc__) > 0)
        self.assertTrue(len(Square.__init__.__doc__) > 0)
        self.assertTrue(len(Square.__str__.__doc__) > 0)

    def test_trivial(self):
        """ Function: test_trivial
                      to test trivial cases
        """
        Base._nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.area(), 25)
        s3 = Square(2, 2)
        self.assertEqual(s3.id, 2)
        self.assertEqual(s3.area(), 4)

    def test_display(self):
        """ Function: test_display
                      to test display cases
        """
        Base._nb_objects = 0
        temp = sys.stdout
        sys.stdout = StringIO()
        s1 = Square(5)
        s1.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(display, out)

        temp = sys.stdout
        sys.stdout = StringIO()
        s3 = Square(2, 2)
        s3.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "  ##\n  ##\n"
        self.assertEqual(display, out)

    def test_str(self):
        """__str__ tests"""
        Base._nb_objects = 0
        temp = sys.stdout
        sys.stdout = StringIO()
        s1 = Square(5)
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "[Square] (1) 0/0 - 5"
        self.assertEqual(display, str(s1))

        Base._nb_objects = 0
        temp = sys.stdout
        sys.stdout = StringIO()
        s3 = Square(2, 2)
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "[Square] (1) 2/0 - 2"
        self.assertEqual(display, str(s3))

if __name__ == '__main__':
    unittest.main()
