import unittest

from pycheck import check


class TestNumber(unittest.TestCase):

	def test_accept_number(self):
		check(3)