from myfuncs import squarefunc, halffunc
import unittest

class testmyfuncs(unittest.TestCase):
	def testsquare(self):
		self.assertEqual(squarefunc(4), 16)

	def testhalf(self):
		self.assertEqual(halffunc(4), 1)

if __name__ == '__main__':
	unittest.main(exit=False)

