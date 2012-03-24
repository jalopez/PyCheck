import unittest

from pycheck import check, CheckError


class TestBasic(unittest.TestCase):
	def test_exists(self):
		check(1).exists()
		self.assertRaises(CheckError, check(None).exists)

	def test_is_None(self):
		check(None).is_None()
		self.assertRaises(CheckError, check(3).is_None)

	def test_check_chain(self):
		check(1).exists().exists()
		self.assertRaises(CheckError, check(3).exists().is_None)

	def test_check_dont(self):
		check(None).dont.exists()
		check(1).dont.is_None()
		self.assertRaises(CheckError, check(3).dont.exists)

	def test_check_variable_name(self):
		try:
			my_var = 3
			check(my_var, 'my_var').dont.exists()
		except CheckError, e:
			self.assertEquals(str(e), "'my_var should not exist'")


class TestNumber(unittest.TestCase):

	def test_accept_number(self):
		check(3)

	#def test_is_number(self):
	#	check(0).is_number()
