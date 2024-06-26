#!/usr/bin/python3
"""Unittest module for the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.Testcase):
    """Unittests for testing FileStorage"""
    def setUp(self):
        """Set up of instances"""
        self.my_storage = FileStorage()

    def test_FileStorage_instance(self):
        """Test for is instance"""
        self.assertIsInstance()
