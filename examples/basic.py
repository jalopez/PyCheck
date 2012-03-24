from pycheck import check

def basic(param1, param2=None):
    check(param1, 'param1').exists()
    check(param2, 'param2').dont.exists()


if __name__ == "__main__":
    basic(3)
    basic(4, 5)
