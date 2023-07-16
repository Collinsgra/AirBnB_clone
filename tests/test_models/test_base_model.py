#!/usr/bin/python3
"""Test cases for models"""

import pep8
import unittest
import os
from models import base_model
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    """Tbase model"""

    def test_unique_id(self):
        """
        test for unique id
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)

    def test_id_type(self):
        """
        test id types
        """
        instance1 = BaseModel()
        self.assertEqual('<class \'str\'>', str(type(instance1.id)))

    def test_exec_file(self):
        """
        tests file execution
        """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertEqual(True, read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertEqual(True, write)
        exec = os.access('models/base_model.py', os.X_OK)
        self.assertEqual(True, exec)

    def test_save(self):

        instance1 = BaseModel()
        attr_updated_before_save = instance1.updated_at
        instance1.save()
        attr_updated_after_save = instance1.updated_at
        self.assertNotEqual(attr_updated_before_save, attr_updated_after_save)

    def test_to_dict(self):

        instance1 = BaseModel()
        instance1_User = User()

        self.assertEqual('<class \'dict\'>', str(type(instance1.to_dict())))

        updated_expected_format = instance1.updated_at.isoformat()
        created_expected_format = instance1.created_at.isoformat()
        class_attr_value_expected = type(instance1_User).__name__
        updated_actual_format = instance1.to_dict()["updated_at"]
        created_actual_format = instance1.to_dict()["created_at"]
        class_attr_value_get = instance1_User.to_dict()['__class__']

        self.assertEqual(updated_expected_format, updated_actual_format)
        self.assertEqual(created_expected_format, created_actual_format)
        self.assertEqual(class_attr_value_expected, class_attr_value_get)


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """tests for pep8"""
        style = pep8.StyleGuide(quiet=True)
        base_mod = "models/base_model.py"
        test_base_mod = "tests/test_models/test_base_model.py"
        result = style.check_files([base_mod, test_base_mod])
        self.assertEqual(result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """tests file base i files"""

    def test_module(self):
        """module"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class(self):
        """doc class checker"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method(self):
        """METHOD STR"""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

