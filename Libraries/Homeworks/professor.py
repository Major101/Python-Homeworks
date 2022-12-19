import random

def main():
    error_count = 3
    points = 10
    level = get_level()

    for _ in range(10):
        x,y = generate_integer(level) , generate_integer(level)
        answer = x + y

        while True:
            print(f'{x} + {y} = ', end='')
            
            u_answer = int(input())
            
            if u_answer == answer:
                break
            else:
                error_count -= 1

            if error_count == 0:
                print('EEE')
                error_count = 3
                points -= 1
                break

    print(f'Score: {points}')

def get_level():
    while True:
        level = int(input("Level: "))
        if 0<level<4:
            return level 

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()