#!/usr/bin/python3
"""Unittest for basemodel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel class"""

    def test_docstrings(self):
        """Check docstrings for BaseModel class"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_functions(self):
        """Check if BaseModel class has all the functions"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_attributes(self):
        """Tests attributes of the BaseModel instance"""
        base_model = BaseModel()
        self.assertEqual(str, type(base_model.id))
        self.assertEqual(datetime, type(base_model.created_at))
        self.assertEqual(datetime, type(base_model.updated_at))

    def test_instance_similarities(self):
        """Check if BaseModel instance are the same"""
        bs1 = BaseModel()
        bs2 = BaseModel()
        self.assertNotEqual(bs1.id, bs2.id)

    def test_init(self):
        """Tests the constructor function of the basemodel"""
        now = datetime.now()
        id = "5"
        bs = BaseModel(id=id, created_at=now.isoformat())

        self.assertEqual(id, bs.id)
        self.assertEqual(now, bs.created_at)

    def test_str(self):
        """Tests the string represantation of the basemodel class"""
        bs = BaseModel()
        string = bs.__str__()
        self.assertIn("[BaseModel] ({})".format(bs.id), string)
        self.assertIn("'id': '{}'".format(bs.id), string)
        self.assertIn("'created_at': {}".format(repr(bs.created_at)), string)
        self.assertIn("'updated_at': {}".format(repr(bs.updated_at)), string)

    def test_save(self):
        """Tests the save function of the basemodel class"""
        bs = BaseModel()
        old_dt = bs.updated_at
        bs.save()
        self.assertLess(old_dt, bs.updated_at)

    def test_to_dict(self):
        """Tests to_dict function of the basemodel class"""
        bs = BaseModel()
        bs_dict = bs.to_dict()
        self.assertEqual(dict, type(bs_dict))
        self.assertEqual(bs.id, bs_dict["id"])
        self.assertEqual("BaseModel", bs_dict["__class__"])
        self.assertEqual(bs.created_at.isoformat(), bs_dict["created_at"])
        self.assertEqual(bs.updated_at.isoformat(), bs_dict["updated_at"])
        self.assertEqual(bs_dict.get("_sa_instance_state", None), None)


if __name__ == "__main__":
    unittest.main()
