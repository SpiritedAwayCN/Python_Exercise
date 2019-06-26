import libs.soldier
import libs.headquarter
import libs.city
import libs.weapon
from libs.schedule import Run

#input_file = open('data/sample.txt', 'r')
input_file = open('data/input.txt', 'r')

def get_number_tuple():
    # 没有do-while真烦
    number_tuple = tuple(map(int, input_file.readline().split()))
    while len(number_tuple) == 0:
        number_tuple = tuple(map(int, input_file.readline().split()))
    return number_tuple

case_number = int(input_file.readline())
for T in range(case_number):
    print("Case %d:"%(T + 1))
    libs.city.City.city_list = []

    libs.headquarter.HeadQuarter.init_element, \
        libs.city.City.N, libs.weapon.Arrow.R, \
        libs.soldier.Lion.K, tle \
        = get_number_tuple()

    libs.soldier.Dragon.init_strength,  \
        libs.soldier.Ninja.init_strength, \
        libs.soldier.Iceman.init_strength, \
        libs.soldier.Lion.init_strength, \
        libs.soldier.Wolf.init_strength, \
        = get_number_tuple()
    
    libs.soldier.Dragon.init_force,  \
        libs.soldier.Ninja.init_force, \
        libs.soldier.Iceman.init_force, \
        libs.soldier.Lion.init_force, \
        libs.soldier.Wolf.init_force, \
        = get_number_tuple()
    
    Run(tle)