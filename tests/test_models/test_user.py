#!/usr/bin/python3
"""tests for users"""

import pep8
import unittest
from models.user import User
from models import user



class Testpep8module(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for the testuser"""
        style = pep8.StyleGuide(quiet=True)
        user_pep8 = "models/user.py"
        test_user_pep8 = "tests/test_models/test_user.py"
        result = style.check_files([user_pep8, test_user_pep8])
        self.assertEqual(result.total_errors, 0)


class TestBaseModelsDocus(unittest.TestCase):
    """test docs for pep8"""

    def test_module(self):
        """search modules"""
        self.assertTrue(len(user.__doc__) > 0)

    def test_class(self):
        """checking the class module doc"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_method(self):
        """checks docstring"""
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

