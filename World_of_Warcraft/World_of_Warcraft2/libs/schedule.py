#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: schedule.py
# modified: 2019-06-28

from .timer import Timer
from .headquarter import HeadQuarter

def run():
    redHQ  = HeadQuarter('red')
    blueHQ = HeadQuarter('blue')
    timer  = Timer()

    while True:

        redHQ.make_soldier(timer)
        blueHQ.make_soldier(timer)

        if redHQ.lose and blueHQ.lose:
            break

        timer.next_hour()