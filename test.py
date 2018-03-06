import unittest

import my_functions

class TestMyFunc(unittest.TestCase):

	def setUp(self):
		pass

	def test_increment_six_6(self):
		self.assertEqual(my_functions.increment_by_six(0), 6)

	def test_multiply_two_2(self):
		self.assertEqual(my_functions.multiply_by_two(2), 4)

if __name__ == '__main__':
	unittest.main()
