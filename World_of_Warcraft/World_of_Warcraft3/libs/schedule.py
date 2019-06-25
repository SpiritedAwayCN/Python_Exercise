from .timer import Timer
from .headquarter import HeadQuarter
from .soldier import Soldier
from .city import City

def check_termin(gametime, tle, redHQ, blueHQ):
    if gametime.total_minute() > tle:
        return True
    if redHQ.enemy_count > 0 or blueHQ.enemy_count >0:
        return True
    return False

def Run(tle):
    redHQ = HeadQuarter('red')
    blueHQ = HeadQuarter('blue')
    gametime = Timer()
    for i in range(City.N + 2):
        City.city_list.append(City(i))

    while True:
        gametime.minute = 0
        redHQ.make_soldier(gametime)
        blueHQ.make_soldier(gametime)
        
        gametime.minute = 5
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for city in City.city_list:
            city.lion_escape(gametime)

        gametime.minute = 10
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for soldier in redHQ.soldier_list:
            soldier.march_next(gametime, blueHQ)
        for soldier in blueHQ.soldier_list:
            soldier.march_next(gametime, redHQ)
        for city in City.city_list:
            city.print_info()
            city.clear_arrived_soldiers()
        
        
        gametime.minute = 35
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for city in City.city_list:
            city.do_stole_weapons(gametime)
        
        gametime.minute = 40
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for city in City.city_list:
            city.do_battle(gametime)

        gametime.minute = 50
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        redHQ.report_element(gametime)
        blueHQ.report_element(gametime)

        gametime.minute = 55
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for city in City.city_list:
            city.soldier_report(gametime)

        gametime.next_hour()