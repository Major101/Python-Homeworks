from random import choice
while True:
    a = int(input('darajani kiriting: '))
    if a > 0:
        b = range(1,a)
        c = choice(b)
        while True:
            d = int(input('raqamni kiriting: '))
            if d > c:
                print('juda katta')
            if d < c:
                print('juda kichik')
            elif d == c:
                print('topdingiz')
                break
        print(c)
        break
    else:
        print('butun son kiriting!')