# test_modellink.py
"""
Tests for ModelLink module.
"""

import unittest
from modellink import ModelLink

class TestModelLink(unittest.TestCase):
    """Test cases for ModelLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelLink()
        self.assertIsInstance(instance, ModelLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
