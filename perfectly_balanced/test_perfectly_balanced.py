import unittest
import perfectly_balanced

class TestBalanced(unittest.TestCase):
    
	def test_even_len(self):
		test_str = "xxxyyy"
		self.assertTrue(perfectly_balanced.balanced(test_str))

if __name__ == '__main__':
    unittest.main()


    # balanced("xxxyyy") => true
# balanced("yyyxxx") => true
# balanced("xxxyyyy") => false
# balanced("yyxyxxyxxyyyyxxxyxyx") => true
# balanced("xyxxxxyyyxyxxyxxyy") => false
# balanced("") => true
# balanced("x") => false