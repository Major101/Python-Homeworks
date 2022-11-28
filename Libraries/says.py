import sys
from saids import hello, goodbye

if len(sys.argv) < 2:
    sys.exit('Ism kiritmading.')

hello(sys.argv[1])
goodbye(sys.argv[1])



    