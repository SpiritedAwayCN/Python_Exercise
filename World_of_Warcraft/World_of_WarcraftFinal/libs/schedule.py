from .timer import Timer
from .headquarter import HeadQuarter
from .soldier import Soldier
from .city import City

def check_termin(gametime, tle, redHQ, blueHQ):
    if gametime.total_minute() > tle:
        return True
    if len(redHQ.enemies) > 1 or len(blueHQ.enemies) > 1:
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

        gametime.minute = 20
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for i in range(City.N):
            City.city_list[i + 1].do_spawn_elements()
        
        gametime.minute = 30
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for i in range(City.N):
            City.city_list[i + 1].do_attain_elements(gametime)

        gametime.minute = 35
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for i in range(City.N):
            City.city_list[i + 1].do_shoot(gametime)
        for i in range(City.N):
            City.city_list[i + 1].after_shoot()

        gametime.minute = 38
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for i in range(City.N):
            City.city_list[i + 1].do_battle(gametime)
        
        gametime.minute = 40
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for i in range(City.N, 0, -1):
            City.city_list[i].do_send_elements(redHQ)
        for i in range(City.N):
            City.city_list[i + 1].do_send_elements(blueHQ)
        for i in range(City.N):
            City.city_list[i + 1].after_war(gametime)

        gametime.minute = 50
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        redHQ.report_element(gametime)
        blueHQ.report_element(gametime)

        gametime.minute = 55
        if check_termin(gametime, tle, redHQ, blueHQ):
            break
        for i in range(1, City.N + 1):
            City.city_list[i].soldier_report(gametime, redHQ)
        for sd in blueHQ.enemies:
            sd.report_weapons(gametime)
        for sd in redHQ.enemies:
            sd.report_weapons(gametime)
        for i in range(1, City.N + 1):
            City.city_list[i].soldier_report(gametime, blueHQ)

        gametime.next_hour()