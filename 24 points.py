import random

oper_tuple = '+','-','*','/','(',')'

while True:
    number_table = []
    for i in range(4):
        number_table.append(random.randint(1,13))
    for i in number_table:
        print(i, end=' ')
    print('')

    command = input()
    if command=="quit":
        break
    elif command=="no":
        pass
    elif command=="help":
        pass
    elif command=="next":
        continue
    invalid_expression = False
    
    expression = ''
    for ch in command:
        if ch in oper_tuple:
            expression+= ' '+ch+' '
        elif ch.isdigit() or ch!='.':
            expression+=ch
        else:
            print("Invalid expression!")
            invalid_expression = True
            break
    if invalid_expression:
        continue
    