#!/usr/bin/python3
"""Unittest belongs to test file: class and methods"""

import pep8
import unittest
from models import city
from models.city import City


class testpep8_beseModel(unittest.TestCase):
    """Verify pep8"""

    def test_pep8(self):
        """it test for base file and also test for test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        city_pep8 = "models/city.py"
        test_city_pep8 = "tests/test_models/test_city.py"
        result = style.check_files([city_pep8, test_city_pep8])
        self.assertEqual(result.total_errors, 0)


class TestDocs_basemode(unittest.TestCase):
    """it tests documents in the strings for base and test_base files"""

    def test_unit(self):
        """it restrain module documents strings"""
        self.assertTrue(len(city.__doc__) > 0)

    def test_category(self):
        """it restrain class documents strings"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_mode(self):
        """It restrain method documents strings"""
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

