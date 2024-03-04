import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertNotEqual(model.created_at, model.updated_at)

    def test_str_representation(self):
        model = BaseModel()
        string_repr = str(model)
        self.assertIn("BaseModel", string_repr)
        self.assertIn(model.id, string_repr)

    def test_save_updates_updated_at(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_unique_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_attribute_change_updates_updated_at(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.some_attribute = "some_value"
        self.assertEqual(original_updated_at, model.updated_at)

    def test_serialization_deserialization(self):
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertNotEqual(model.updated_at, new_model.updated_at)

    def test_equality(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertEqual(model1, model1)
        self.assertNotEqual(model1, model2)

    def test_update_attribute_updates_updated_at(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.some_attribute = "some_value"
        model.save()
        self.assertEqual(original_updated_at, model.updated_at)

    def test_future_updated_at(self):
        model = BaseModel()
        self.assertLessEqual(model.updated_at, datetime.now())

    def test_from_string_to_instance(self):
        model = BaseModel()
        model_dict = model.to_dict()
        model_str = str(model_dict)
        new_model = BaseModel(**eval(model_str))
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertNotEqual(model.updated_at, new_model.updated_at)


if __name__ == '__main__':
    unittest.main()
