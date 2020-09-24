import unittest
import perfectly_balanced

class TestBalanced(unittest.TestCase):
    
	def test_even(self):
		test_str = "xxxyyy"
		self.assertTrue(perfectly_balanced.balanced(test_str))

	def test_odd(self):
		test_str = "xxxyyyx"
		self.assertFalse(perfectly_balanced.balanced(test_str))

	def test_empty(self):
		test_str = ""
		self.assertTrue(perfectly_balanced.balanced(test_str))

if __name__ == '__main__':
    unittest.main()
