from validators import *


def check(value, var_name = None):
    return VariableValidator(value, var_name, check.print_validations)

check.print_validations = False

### Decorators

def only_warn(fn):
    """
        Substitute CheckError exceptions by warnings
    """
    def decorator(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except CheckError, e:
            print 'Warning: ' + str(e)
    return decorator

def print_validations(fn):
    """
        Print all validations that are going to be executed
    """
    def decorator(*args, **kwargs):
        # TODO: Find a better way to notify validation classes about print validations
        check.print_validations = True
        fn(*args, **kwargs)
        check.print_validations = False
    return decorator
