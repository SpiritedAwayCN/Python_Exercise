import operator
from .stack import Stack

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        pass
    return False

def calc(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2
    else:
        raise Exception("Unexpected operator '"+oper+"'!")

class Expression:
    __oper_tuple = '+','-','*','/','(',')'
    __priority = {'*':3, '/':3, '+':2, '-':2, '(':1}
    def __init__(self, expr):
        self.expression = ''
        for ch in expr:
            if ch in self.__oper_tuple:
                self.expression+= ' '+ch+' '
            elif ch.isdigit() or ch=='.':
                self.expression+=ch
            elif ch!=' ':
                raise Exception("Invalid expression!")
        self.token_table = self.expression.split()

    def judge(self, number_table):
        number_list = []
        for token in self.token_table:
            if is_number(token):
                num = float(token)
                number_list.append(num)
        if not operator.eq(sorted(number_list), sorted(number_table)):
            raise Exception("You should use the numbers given above!")

    def Get_value(self):
        opStack = Stack()
        numStack = Stack()
        for token in self.token_table:
            if(is_number(token)):
                numStack.push(float(token))
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                toptoken = opStack.pop()
                while toptoken != '(':
                    num2 = numStack.pop()
                    num1 = numStack.pop()
                    numStack.push(calc(num1, num2, toptoken))
                    toptoken = opStack.pop()
            else:
                if token not in Expression.__oper_tuple:
                    raise Exception("Unknown token '" + token + "'!")
                while (not opStack.empty()) and Expression.__priority[opStack.top()]>=Expression.__priority[token]:
                    oper = opStack.pop()
                    num2 = numStack.pop()
                    num1 = numStack.pop()
                    numStack.push(calc(num1, num2, oper))
                opStack.push(token)
        while not opStack.empty():
            oper = opStack.pop()
            num2 = numStack.pop()
            num1 = numStack.pop()
            numStack.push(calc(num1, num2, oper))
        ans = numStack.pop()
        if not numStack.empty():
            raise Exception("Too many numbers!")
        return ans

# while True:
#     string = input()
#     calc_task = Expression(string)

#     try:
#         print("%.3f"%calc_task.Get_value())
#     except Exception as identifier:
#         print(identifier)