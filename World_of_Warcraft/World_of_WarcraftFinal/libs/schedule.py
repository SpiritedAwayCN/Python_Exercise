#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: schedule.py
# modified: 2019-06-28

__all__ = ["run"]

from .timer import timer
from .headquarter import HeadQuarter
from .soldier import Soldier
from .city import City

def run(TLE):

    redHQ = HeadQuarter('red')
    blueHQ = HeadQuarter('blue')
    HQS = (redHQ, blueHQ)
    citys = City.city_list = [ City(i) for i in range(City.N + 2) ]

    def is_finished():
        return timer.total > TLE or any([ len(hq.enemies) > 1 for hq in HQS ])

    timer.reset()

    while True:

        timer.minute = 0
        for hq in HQS:
            hq.make_soldier()

        timer.minute = 5
        if is_finished():
            break
        for c in citys:
            c.lion_escape()

        timer.minute = 10
        if is_finished():
            break
        for hq, ohq in zip(HQS, reversed(HQS)):
            for s in hq.soldiers:
                s.march_next(ohq)

        for c in citys:
            c.print_info()
            c.clear_arrived_soldiers()

        timer.minute = 20
        if is_finished():
            break
        for c in citys[1:]:
            c.do_spawn_elements()

        timer.minute = 30
        if is_finished():
            break
        for c in citys[1:]:
            c.do_attain_elements()

        timer.minute = 35
        if is_finished():
            break
        for c in citys[1:]:
            c.do_shoot()
        for c in citys[1:]:
            c.after_shoot()

        timer.minute = 38
        if is_finished():
            break
        for c in citys[1:]:
            c.do_battle()

        timer.minute = 40
        if is_finished():
            break

        for c in citys[-2:0:-1]:
            c.do_send_elements(redHQ)
        for c in citys[1:]:
            c.do_send_elements(blueHQ)
        for c in citys[1:]:
            c.after_war()

        timer.minute = 50
        if is_finished():
            break
        for hq in HQS:
            hq.report_element()

        timer.minute = 55
        if is_finished():
            break
        for c in citys[1:]:
            c.soldier_report(redHQ)
        for hq in reversed(HQS):
            for s in hq.enemies:
                s.report_weapons()
        for c in citys[1:]:
            c.soldier_report(blueHQ)

        timer.next_hour()