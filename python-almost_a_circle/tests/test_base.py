#!/usr/bin/python3
""""""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """"""
    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_empty(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)


    def test_list_id(self):
        self.assertEqual([20, 3, 5], Base([20, 3, 5]).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'Hidalgo'), Base(bytearray(b'Hidalgo')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)




    

    




if __name__ == "__main__":
    unittest.main()
