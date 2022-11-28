import cowsay
import sys

if len(sys.argv) < 2:
    sys.exit('Ism kiritmading.')

cowsay.fox('Salom! , ' + sys.argv[1])