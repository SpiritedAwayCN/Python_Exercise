#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: headquarter.py
# modified: 2019-06-28

__all__ = ["HeadQuarter"]

from .timer import timer
from .soldier import Dragon, Ninja, Iceman, Lion, Wolf

class HeadQuarter(object):

    INIT_ELEMENT = 0
    SOLDIER_ORDER = {
        'red':  (Iceman, Lion, Wolf, Ninja, Dragon),
        'blue': (Lion, Dragon, Ninja, Iceman, Wolf),
    }

    def __init__(self, name):
        self._name = name
        self._enemies = []
        self._element = self.INIT_ELEMENT
        self._soldiers = []
        self._soldier_id = 0
        self._soldier_iter = self._soldier_generator(self.SOLDIER_ORDER[self._name])

    @property
    def name(self):
        return self._name

    @property
    def soldiers(self):
        return self._soldiers

    @property
    def enemies(self):
        return self._enemies

    def __str__(self):
        return "%s %s" % (
                self._name,
                self.__class__.__name__.lower(),
            )

    def add_elements(self, number):
        if self._element + number >= 0:
            self._element += number
            return True
        return False

    def _soldier_generator(self, SOLDIERS):
        while True:
            for _Soldier in SOLDIERS:
                while True:
                    if self._element >= _Soldier.INIT_STRENGTH:
                        self._soldier_id += 1
                        yield _Soldier(self, self._soldier_id, self._element)
                        break
                    else:
                        yield None

    def make_soldier(self):
        soldier = next(self._soldier_iter)
        if soldier is None:
            return

        self._element -= soldier.INIT_STRENGTH
        self._soldiers.append(soldier)

        print("%s %s born" % (timer, soldier) )
        if soldier.remark != None:
            print(soldier.remark)

    def report_element(self):
        print("%s %s elements in %s" % (timer, self._element, str(self)) )