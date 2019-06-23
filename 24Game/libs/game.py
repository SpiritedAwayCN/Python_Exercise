import random

def get_number():
    number_table = []
    for i in range(4):
        number_table.append(float(random.randint(1,13)))
    return number_table

def Game_Run():
    number_table = get_number()

    for i in number_table:
        print(i, end = ' ')
    print('')

    command = input()
    if command=="quit":
        return True
    elif command=="no":
        pass
    elif command=="help":
        pass
    elif command=="next":
        return False
    


def Game_Main():
    print("Game has started!")
    print("============================")
    print("Enter a expression with a result of 24 by using given numbers.")
    print('Enter "no" if there is no any solution')
    print("Sample: (4-2)*(8+4)")
    print("============================")
    print("Commands:")
    print("help\tShow the solution")
    print("next\tSkip current puzzle")
    print("quit\tReturn to calculator")
    print('')

    while True:
        if Game_Run():
            break

