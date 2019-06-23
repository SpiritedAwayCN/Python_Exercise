import random
import sys
from .expression import Expression
from .calculator import get_solution_array

def get_number():
    number_table = []
    for i in range(4):
        number_table.append(float(random.randint(1,13)))
    return number_table

def equal_float(a, b):
    return abs(a-b) < sys.float_info.epsilon

def Game_Run():
    number_table = get_number()
    print('')
    for i in number_table:
        print("%.0f"%i, end = ' ')
    print('')
    solution_array = get_solution_array(number_table)
    while True:
        command = input()
        if command=="quit":
            return True
        elif command=="no":
            if len(solution_array)==0:
                print("Congratulations! No solution.")
                return False
            print("There exists solution, try again!")
            continue
        elif command=="help":
            if len(solution_array)==0:
                print("No solution.")
            else:
                for i in solution_array:
                    print(i)
            return False
        elif command=="next":
            return False
        try:
            calc_task = Expression(command)
            calc_task.judge(number_table)
            ans = calc_task.Get_value()
            print("=%.3f"%ans)
            if(equal_float(ans,24)):
                print("Congratulations!")
                return False
            else:
                print("Oops! The value is not 24! Try again!")
        except Exception as identifier:
            print(identifier)
    


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

    while True:
        if Game_Run():
            break