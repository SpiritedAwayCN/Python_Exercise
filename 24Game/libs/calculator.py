from .instruction import Instruction

number_array = []
solution_array = []

def initialize():
    global number_array, solution_array
    number_array = []
    solution_array = []

def get_numberList(string):
    numstr = string.split()
    if len(numstr) != 4:
        raise Exception("The number of integer should be 4!")
    number_list = []
    for st in numstr:
        number_list.append(float(st))
    return number_list

def equal_float(a, b):
    # 若采用sys.float_info.epsilon，则3 3 8 8会被认为无解
    return abs(a-b) < 1e-6

def dfs(left):
    global number_array, solution_array 
    if left == 1:
        for i in number_array:
            if equal_float(i, 0):
                continue
            if equal_float(i, 24):
                return True
            else:
                return False
    for i in range(4):
        if equal_float(number_array[i], 0):
            continue
        for j in range(4):
            if i==j or equal_float(number_array[j], 0):
                continue
            num1, num2 = number_array[i], number_array[j]
            for law in range(4):
                number_array[i] = 0
                if law == 0:
                    number_array[j] = num1 + num2
                elif law == 1 and num1 < num2:
                    continue
                elif law == 1:
                    number_array[j] = num1 - num2
                elif law == 2:
                    number_array[j] = num1 * num2
                else:
                    number_array[j] = num1 / num2
                solution_array.append(Instruction(num1, num2, law, number_array[j]))
                if dfs(left - 1):
                    return True
                solution_array.pop()
                number_array[i] = num1
                number_array[j] = num2
    return False

def Calc_Main(string):
    initialize()
    global number_array
    try:
        number_list = get_numberList(string)
    except Exception as identifier:
        print(identifier)
        return
    number_array = number_list[:]
    if(dfs(4)):
        for i in solution_array:
            print(i)
    else:
        print("No solution!")

def get_solution_array(number_list):
    initialize()
    global number_array
    number_array = number_list[:]
    dfs(4)
    return solution_array