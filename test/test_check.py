from check import check
import unittest

class TestBasicUsage(unittest.TestCase):

	def test_accept_number(self):
		self.assertTrue(check(3))