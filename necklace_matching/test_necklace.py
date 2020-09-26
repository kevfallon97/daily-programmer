import unittest
import necklace

class TestNecklace(unittest.TestCase):

	def test_valid_necklace(self):
		a = "nicole"
		b = "icolen"
		self.assertTrue(necklace.same_necklace(a,b))

	def test_invalid_necklace(self):
		a = "nicole"
		b = "icolne"
		self.assertFalse(necklace.same_necklace(a,b))

if __name__ == '__main__':
	unittest.main()