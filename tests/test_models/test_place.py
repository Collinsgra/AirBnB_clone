#!/usr/bin/python3
"""Unittest for place file: class and mode"""

import pep8
import unittest
from models import place
from models.place import Place


class testpep8_beseModel(unittest.TestCase):
    """Verify pep8"""

    def test_pep8(self):
        """it test for base file and also test for test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        place_pep8 = "models/place.py"
        test_place_pep8 = "tests/test_models/test_place.py"
        result = style.check_files([place_pep8, test_place_pep8])
        self.assertEqual(result.total_errors, 0)


class TestDocs_basemode(unittest.TestCase):
    """it test document strings for base and also for test_base files"""

    def test_unit(self):
        """it restrain the module document strings"""
        self.assertTrue(len(place.__doc__) > 0)

    def test_category(self):
        """it restrain the class document strings"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_mode(self):
        """it restrain the method document strings"""
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

