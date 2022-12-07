from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print('2ni kvadrati 4')
    try:
        assert square(3) == 9
    except AssertionError:
        print('2ni kvadrati 4')
    try:
        assert square(4) == 16
    except AssertionError:
        print('4ni kvadrati 4')
    try:
        assert square(0) == 0
    except AssertionError:
        print('0ni kvadrati 0')

main()