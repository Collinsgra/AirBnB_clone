#!/usr/bin/python3
"""Unittest for review file: class and methods"""

import pep8
import unittest
from models import review
from models.review import Review


class testpep8_beseModel(unittest.TestCase):
    """Verify pep8"""

    def test_pep8(self):
        """it test for base file and also test for test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        review_pep8 = "models/review.py"
        test_review_pep8 = "tests/test_models/test_review.py"
        result = style.check_files([review_pep8, test_review_pep8])
        self.assertEqual(result.total_errors, 0)


class TestDocs_basemode(unittest.TestCase):
    """it test document strings for base and also test for test_base files"""

    def test_unit(self):
        """it restrain the module document strings"""
        self.assertTrue(len(review.__doc__) > 0)

    def test_category(self):
        """it restrain the class document strings"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_mode(self):
        """it restrain the method docstrings"""
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

