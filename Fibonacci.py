
def Fibonacci(max_num):
    a, b, cont = 0, 1, 0
    while cont<=max_num:
        yield a
        a, b = b, b + a
        cont += 1

x = Fibonacci(10)

for i in x:
    print(i, end = ' ')
print('')