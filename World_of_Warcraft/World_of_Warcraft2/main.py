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

    libs.soldier.Dragon.init_strength,  \
        libs.soldier.Ninja.init_strength, \
        libs.soldier.Iceman.init_strength, \
        libs.soldier.Lion.init_strength, \
        libs.soldier.Wolf.init_strength, \
        = map(int, input_file.readline().split())
    
    Run()