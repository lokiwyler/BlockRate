# test_blockrate.py
"""
Tests for BlockRate module.
"""

import unittest
from blockrate import BlockRate

class TestBlockRate(unittest.TestCase):
    """Test cases for BlockRate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockRate()
        self.assertIsInstance(instance, BlockRate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockRate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
