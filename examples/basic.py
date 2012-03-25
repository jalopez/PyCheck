from pycheck import check, only_warn, print_validations

def basic(param1, param2=None):
    check(param1, 'param1').exists()
    check(param2, 'param2').dont.exists()

@only_warn
def with_decorator(param1 = None):
    check(param1, 'param1').exists()

@print_validations
def with_print(param1 = None, param2 = None):
    check(param1, 'param1').exists()
    check(param2, 'param2').dont.exists()

if __name__ == "__main__":
    basic(2)
    print "+ With only_warn decorator"
    with_decorator()
    print "+ With print validations"
    with_print(3)
    print "+ Exceptions"
    basic(2,3)
