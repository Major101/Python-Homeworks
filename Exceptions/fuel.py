def main():
    input_data = fraction_input()
    display(input_data)

def fraction_input():
    while True:
        try:
            numenator, denumator = input('Fraction: ').split('/')
        
            numenator = int(numenator)
            denumator = int(denumator)

            fraction = numenator / denumator
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if fraction <= 1:
                return fraction * 100

def display(number):
    if number <= 1:
        print('E')
    elif number >= 99:
        print('F')
    else:
        print(f'{number:.0f}%')

main()