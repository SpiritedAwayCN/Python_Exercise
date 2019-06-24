import libs.soldier
import libs.headquarter
from libs.schedule import Run

#input_file = open('data/sample.txt', 'r')
input_file = open('data/input.txt', 'r')

case_number = int(input_file.readline())
for T in range(case_number):
    print("Case:%d"%(T + 1))

    libs.headquarter.HeadQuarter.init_element \
        = int(input_file.readline())

    libs.soldier.Dragon.strength,  \
        libs.soldier.Ninja.strength, \
        libs.soldier.Iceman.strength, \
        libs.soldier.Lion.strength, \
        libs.soldier.Wolf.strength, \
        = map(int, input_file.readline().split())
    
    Run()