PyCheck
=======
Python parameter validator. This library can be used to validate the
input parameters of a function (or any other variable) against a set 
of restrictions. It can be seen as a precondition validator

Basic Usage
-----------
* Import the library:

    ```python
    from pycheck import check
    ```

* Use it inside any function

    ```python
    def my_func(param1, param2):
        check(param1).exists()
        check(param2).is_number().positive()
    ```

Valid assertions
----------------
TODO
