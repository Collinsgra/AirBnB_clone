#!/usr/bin/python3
"""Unittest for amenity file: class and methods"""

import pep8
import unittest
from models import amenity
from models.amenity import Amenity


class testpep8_beseModel(unittest.TestCase):
    """Verify pep8"""

    def test_pep8(self):
        """it test for base file and also test for test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        amen_pep8 = "models/amenity.py"
        test_amen_pep8 = "tests/test_models/test_amenity.py"
        result = style.check_files([amen_pep8, test_amen_pep8])
        self.assertEqual(result.total_errors, 0)


class TestDocs_basemode(unittest.TestCase):
    """it test document strings for base and also for test_base files"""

    def test_unit(self):
        """it restrain a module document in strings"""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_category(self):
        """it restrain the class document a strings"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_mode(self):
        """its restrain method document a strings"""
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

