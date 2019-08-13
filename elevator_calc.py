import math
import decimal
import os

class MuChart:
    def __init__(self, string):
        self.m = decimal.Decimal(string[0])
        self.mu = decimal.Decimal(string[1])
    def __lt__(self, B):
        return self.m < B.m

mu_list = []
def get_mu(value):
    if value < 0:
        raise Exception("M2<0, 无法计算mu")
    index = 0
    while mu_list[index].m <= value and index < len(mu_list):
        index += 1
    if index == len(mu_list):
        return mu_list[-1]
    return (mu_list[index].mu - mu_list[index - 1].mu) / (mu_list[index].m - mu_list[index - 1].m) \
        * (value - mu_list[index].m) + mu_list[index].mu

try:
    infile = open("elevator.txt","r")
    mu_file = open("mu_dict.txt","r")
except FileNotFoundError:
    print("未找到文件")
    os.system("pause")
    exit(0)
for line in infile:
    line = "val_" + line.strip()
    line = line.split('=')
    exec(line[0] + '=decimal.Decimal('+line[1]+')')
for line in mu_file:
    mu_list.append(MuChart(line.strip().split()))
mu_list.sort()
pi = decimal.Decimal(math.pi)
infile.close()
f1 = pow(val_l1, 3) / (3 * val_E * val_I)
print('1. f1 = %e'%f1)
f2 = pow(val_l1, 2) * val_l2 / (3 * val_E * val_I)
print('2. f2 = %e'%f2)
f = (f1 + f2) * val_k
print('3. f = %e'%f)
I2 = val_b1 * pow(val_h1, 3) - val_b2 * pow(val_h2, 3)
I2 /= 12
print("4. I2 = %e"%I2)
beta = 1 / (f * val_C)
print('5. beta = %e'%beta)
M = val_L / pi * pow(beta / (val_E * I2), decimal.Decimal(0.25))
print('*6. M = %e'%M)
print('===========')
M2 = beta * pow(val_L, 4) / (16 * val_E * I2)
print('7. M2 = %e'%M2)
try:
    mu = get_mu(M2)
except Exception as identifier:
    print(identifier)
    os.system("pause")
    exit(0)
print("8. mu =%e"%mu)
print('===========')
F = pi * pi * val_E * I2 / pow(mu * val_L, 2)
print('*9. F = %e'%F)
os.system("pause")
