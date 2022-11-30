import sys

if len(sys.argv) < 2:
    sys.exit('Ism kiritmading.')

for arg in sys.argv[1:]:
    print('Hello, my name is ', arg)