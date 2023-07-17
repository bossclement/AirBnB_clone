#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Creates attributes for classes that i'll need"""
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Deletes all the created class attributes"""
        del cls.storage
        del cls.base

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

    def test_attributes(self):
        """Check for attributes for FileStorage class"""
        path = "file.json"
        self.assertEqual(str, type(self.storage._FileStorage__file_path))
        self.assertEqual(dict, type(self.storage._FileStorage__objects))
        self.assertEqual(self.storage._FileStorage__file_path, path)

    def test_init(self):
        """Test initialization."""
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_all(self):
        """Check all method for filestorage class"""
        store = FileStorage()
        obj = store.all()
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, FileStorage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
