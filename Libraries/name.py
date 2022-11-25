import sys

if len(sys.argv) < 2:
    sys.exit('Ism kiritmading.')
elif len(sys.argv) > 2:
    sys.exit('Keraksiz Argumentlar bor.')

print('Hello, my name is ', sys.argv[1])

    