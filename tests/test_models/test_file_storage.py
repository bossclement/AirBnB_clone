#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for FileStorage class"""

    def test_docstrings(self):
        """Check docstrings for FileStorage class"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_functions(self):
        """Check if FileStorage class has all the functions"""
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_instance_similarities(self):
        """Check if BaseModel instance are the same"""
        fl1 = FileStorage()
        fl2 = FileStorage()
        self.assertEqual(fl1.all(), fl2.all())


if __name__ == "__main__":
    unittest.main()
