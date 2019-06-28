import libs.soldier
import libs.headquarter
import libs.city
import libs.weapon
from libs.schedule import run

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

    libs.headquarter.HeadQuarter.INIT_ELEMENT, \
        libs.city.City.N, libs.weapon.Arrow.R, \
        libs.soldier.Lion.K, tle \
        = get_number_tuple()

    libs.soldier.Dragon.INIT_STRENGTH,  \
        libs.soldier.Ninja.INIT_STRENGTH, \
        libs.soldier.Iceman.INIT_STRENGTH, \
        libs.soldier.Lion.INIT_STRENGTH, \
        libs.soldier.Wolf.INIT_STRENGTH, \
        = get_number_tuple()

    libs.soldier.Dragon.INIT_FORCE,  \
        libs.soldier.Ninja.INIT_FORCE, \
        libs.soldier.Iceman.INIT_FORCE, \
        libs.soldier.Lion.INIT_FORCE, \
        libs.soldier.Wolf.INIT_FORCE, \
        = get_number_tuple()

    run(tle)