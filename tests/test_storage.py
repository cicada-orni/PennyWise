import unittest
import os
from src.storage import StorageManager

class TestStorage(unittest.TestCase):
    # initial function before every test
    def setUp(self) -> None:
        self.test_file = 'test_data.json'
        self.local_storage = StorageManager(self.test_file)

    # clean up function
    def tearDown(self) -> None:
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self) -> None:
        """Testing local storage saving and loading data"""
        data = [{"id": "123", "amount": 50}]
        self.local_storage.save(data)
        loaded_data = self.local_storage.load()
        self.assertEqual(loaded_data, data)

    def test_load_missing_file(self):
        """Testing missing file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        loaded_data = self.local_storage.load()
        self.assertEqual(loaded_data, [])