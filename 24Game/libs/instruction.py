class Instruction:
    def __init__(self, operand1, operand2, opertor, ans):
        self.num1 = operand1
        self.num2 = operand2
        self.ans = ans
        if opertor == 0:
            self.oper = '+'
        elif opertor == 1:
            self.oper = '-'
        elif opertor == 2:
            self.oper = '*'
        else:
            self.oper = '/'

    def __myFloat2Str(self, number):
        if number.is_integer():
            return "{:.0f}".format(number)
        else:
            return "{:.3f}".format(number)

    def __str__(self):
        string = self.__myFloat2Str(self.num1)
        string += ' ' + self.oper + ' '
        string += self.__myFloat2Str(self.num2)
        string += ' = '
        string += self.__myFloat2Str(self.ans)
        return string