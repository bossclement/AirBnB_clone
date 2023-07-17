#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class TestBaseModel(unittest.TestCase):
    """Unittest for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Creates attributes for classes that i'll need"""
        cls.storage = FileStorage()
        cls.base = BaseModel()
        cls.user = User()
        cls.state = State()
        cls.city = City()
        cls.amenity = Amenity()
        cls.place = Place()
        cls.review = Review()

    @classmethod
    def tearDownClass(cls):
        """Deletes all the created class attributes"""
        del cls.storage
        del cls.base
        del cls.user
        del cls.state
        del cls.city
        del cls.amenity
        del cls.place
        del cls.review

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

    def test_reload(self):
        """Test reload function for FileStorage class"""
        try:
            bs = BaseModel()
            with open("file.json", "w", encoding="utf-8") as f:
                key = "{}.{}".format(type(bs).__name__, bs.id)
                json.dump({key: bs.to_dict()}, f)
            self.storage.reload()
            store = FileStorage._FileStorage__objects
            self.assertIn("BaseModel." + bs.id, store)
        except Exception:
            self.fail()

    def test_save(self):
        """Check save method of FileStorage method"""
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.base.id, save_text)
            self.assertIn("User." + self.user.id, save_text)
            self.assertIn("State." + self.state.id, save_text)
            self.assertIn("Place." + self.place.id, save_text)
            self.assertIn("City." + self.city.id, save_text)
            self.assertIn("Amenity." + self.amenity.id, save_text)
            self.assertIn("Review." + self.review.id, save_text)
            

if __name__ == "__main__":
    unittest.main()
