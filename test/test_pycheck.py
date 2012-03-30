import unittest

from pycheck import check, only_warn
from validators import CheckError


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

    
    def test_check_dont(self):
        check(None).dont.exists()
        check(1).dont.is_None()
        self.assertRaises(CheckError, check(3).dont.exists)
        # Dont only applies once
        check(None).dont.exists().is_None()
        # Chaining dont's
        check(None).dont.exists().dont.exists()


    def test_check_chain(self):
        check(1).exists().exists()
        self.assertRaises(CheckError, check(3).exists().is_None)


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


    def test_equals(self):
        check(None).equals(None)
        check("hello").equals("hello")
        check(2).equals(2)
        check(2).dont.equals(3)
        check(2).dont.equals("2")

    
    def test_distinct(self):
        check(3).distinct(None)
        check("a").distinct("b")
        check(3).dont.distinct(3)


    def test_gt(self):
        check(3).gt(2)
        check("b").gt("a")
        check("2").gt(1)
        check(1).dont.gt("a")
        check(1).gt(0.99)

    def test_ge(self):
        check(2).ge(2).ge(1)
        check(1).dont.ge(2)
        check(1).gt(-2).ge(1)

class TestNumber(unittest.TestCase):

    def test_accept_number(self):
        check(3)

    def test_is_number(self):
        check(0).is_number()
        check("hello").dont.is_number()
        self.assertRaises(CheckError, check("hello").is_number)
        self.assertRaises(CheckError, check(3).dont.is_number)

    def test_is_int(self):
        check(0).is_int()
        check(2.3).dont.is_int()
        check("hello").dont.is_int()
        self.assertRaises(CheckError, check(2.3).is_int)
        self.assertRaises(CheckError, check("hello").is_int)


    def test_is_number_with_booleans(self):
        check(True).is_int()
        check(1).equals(True)
        check(0).equals(False)
        check(2).dont.equals(False).dont.equals(True)
        check(-1).dont.equals(False)

if __name__ == "__main__":
    unittest.main()
