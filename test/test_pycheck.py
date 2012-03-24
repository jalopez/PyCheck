import unittest

from pycheck import check, CheckError


class TestBasic(unittest.TestCase):
	def test_exists(self):
		check(1).exists()

		checker = check(None)
		self.assertRaises(CheckError, checker.exists)

	def test_is_None(self):
		check(None).is_None()

		checker = check(3)
		self.assertRaises(CheckError, checker.is_None)

	def test_chain(self):
		check(1).exists().exists()

class TestNumber(unittest.TestCase):

	def test_accept_number(self):
		check(3)

	#def test_is_number(self):
	#	check(0).is_number()
