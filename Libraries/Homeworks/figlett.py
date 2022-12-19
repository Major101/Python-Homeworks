from pyfiglet import Figlet, FontNotFound
from random import choice
import sys

options = ['-f', '--font']

def main():
    myfont = get_font()
    
    word = input("Input: ")

    display(word, myfont)

def display(text, font):
    figlet = Figlet()
    
    if font != 0: 
        try:
            figlet.setFont(font=font)
        except FontNotFound:
            sys.exit('Notogri font berildi.')
    else:
        font = choice(figlet.getFonts())
        figlet.setFont(font=font)

    print('Output: ')
    print(figlet.renderText(text))
    
def get_font():
    if len(sys.argv) == 3:
        if sys.argv[1] in options:
            return sys.argv[2]
    else:
        return 0

if __name__ == '__main__':
    main()