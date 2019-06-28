#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: schedule.py
# modified: 2019-06-28

from .timer import timer
from .headquarter import HeadQuarter
from .soldier import Soldier
from .city import City

__all__ = ["run"]

def run(TLE):

    redHQ  = HeadQuarter('red')
    blueHQ = HeadQuarter('blue')
    HQS = (redHQ, blueHQ)
    citys = City.city_list = [ City(i) for i in range(City.N + 2) ]

    def _is_finished():
        return timer.total > TLE or any([ hq.enemy_count > 0 for hq in HQS ])

    timer.reset()
    while True:

        timer.minute = 0
        for hq in HQS:
            hq.make_soldier()

        timer.minute = 5
        if _is_finished():
            break
        for city in citys:
            city.lion_escape()

        timer.minute = 10
        if _is_finished():
            break
        for hq, ohq in zip(HQS, reversed(HQS)):
            for s in hq.soldiers:
                s.march_next(ohq)
        for city in citys:
            city.print_info()
            city.clear_arrived_soldiers()

        timer.minute = 35
        if _is_finished():
            break
        for city in citys:
            city.do_stole_weapons()

        timer.minute = 40
        if _is_finished():
            break
        for city in citys:
            city.do_battle()

        timer.minute = 50
        if _is_finished():
            break
        for hq in HQS:
            hq.report_element()

        timer.minute = 55
        if _is_finished():
            break
        for city in citys:
            city.soldier_report()

        timer.next_hour()