# test_storagesync.py
"""
Tests for StorageSync module.
"""

import unittest
from storagesync import StorageSync

class TestStorageSync(unittest.TestCase):
    """Test cases for StorageSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StorageSync()
        self.assertIsInstance(instance, StorageSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StorageSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
