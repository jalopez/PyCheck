from pycheck import check, only_warn

def basic(param1, param2=None):
    check(param1, 'param1').exists()
    check(param2, 'param2').dont.exists()

@only_warn
def with_decorator(param1 = None):
    check(param1, 'param1').exists()

if __name__ == "__main__":
    print "With only_warn decorator"
    with_decorator()
    print "With regular exceptions"
    basic(3)
    basic(4, 5)
