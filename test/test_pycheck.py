import unittest

from pycheck import check, CheckError, only_warn


class TestBasic(unittest.TestCase):
    # As check method raises an exception if validation fails,
    # most tests don't have assertions (unittest does not have
    # any assertion for an exception not being produced). 
    # If something goes wrong, an exception will be raised and 
    # the test will fail

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
        # Dont only applies once
        check(None).dont.exists().is_None()
        # Chaining dont's
        check(None).dont.exists().dont.exists()

    def test_check_with_variable_name(self):
        try:
            my_var = 3
            check(my_var, 'my_var').dont.exists()
        except CheckError, e:
            self.assertEquals(str(e), 'my_var should not exist')

    def test_only_warn_decorator(self):
        @only_warn
        def my_func(param1):
            check(param1).exists()
        my_func(None) # Should not raise an exception

class TestNumber(unittest.TestCase):

    def test_accept_number(self):
        check(3)

    #def test_is_number(self):
    #   check(0).is_number()
