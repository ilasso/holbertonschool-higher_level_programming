#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ Class: TestRectangle: to test class Rectangle
               functions must be inic by test_
               test class name could by named anyway
    """

    def test_doc(self):
        """ Function: test_doc
                      to test if have documentation
        """
        Base._Base__nb_objects = 0
        self.assertTrue(len(rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__init__.__doc__) > 0)
        self.assertTrue(len(Rectangle.area.__doc__) > 0)
        self.assertTrue(len(Rectangle.display.__doc__) > 0)

    def test_trivial(self):
        """ Function: test_trivial
                      to test trivial cases
        """
        Base._nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(10, 2, 0, 0, None)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 20)
        self.assertEqual(r4.area(), 20)

        x = r1.x
        y = r1.y
        width = r1.width
        height = r1.height
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(width, 10)
        self.assertEqual(height, 2)
        x = r2.x
        y = r2.y
        width = r2.width
        height = r2.height
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(width, 2)
        self.assertEqual(height, 10)
        x = r3.x
        y = r3.y
        width = r3.width
        height = r3.height
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(width, 10)
        self.assertEqual(height, 2)
        x = r4.x
        y = r4.y
        width = r4.width
        height = r4.height
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(width, 10)
        self.assertEqual(height, 2)
        r4.x = 24
        self.assertEqual(r4.x, 24)
        r3.y = 55
        self.assertEqual(r3.y, 55)
        r2.width = 97
        self.assertEqual(r2.width, 97)
        r1.height = 33
        self.assertEqual(r1.height, 33)

    def test_domain(self):
        """domain tests"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2, 0, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, "2", 0, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0", 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0", 12)
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 0, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 0, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, -1, 0, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1, 12)

    def test_display(self):
        """display tests"""
        temp = sys.stdout
        sys.stdout = StringIO()
        r5 = Rectangle(2, 10)
        r5.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "##\n##\n##\n##\n##\n##\n##\n##\n##\n##\n"
        self.assertEqual(display, out)

        temp = sys.stdout
        sys.stdout = StringIO()
        r6 = Rectangle(1, 1)
        r6.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "#\n"
        self.assertEqual(display, out)

        temp = sys.stdout
        sys.stdout = StringIO()
        r7 = Rectangle(2, 3, 2, 2)
        r7.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(display, out)

        temp = sys.stdout
        sys.stdout = StringIO()
        r8 = Rectangle(3, 2, 1, 0)
        r8.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = " ###\n ###\n"
        self.assertEqual(display, out)

    def test_str(self):
        temp = sys.stdout
        sys.stdout = StringIO()
        r7 = Rectangle(4, 6, 2, 1, 12)
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = temp
        display = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(display, str(r7))

if __name__ == '__main__':
    unittest.main()
