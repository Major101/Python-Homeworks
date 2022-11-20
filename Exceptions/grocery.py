ITEMS = {}

while True:
    try:
        item = input(': ').title()

        if item in ITEMS:
            ITEMS[item] += 1
        else:
            ITEMS[item] = 1

    except EOFError:
        for item in sorted(ITEMS.keys()):
            print(ITEMS[item], item)

        break