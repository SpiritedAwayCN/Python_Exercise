#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: headquarter.py
# modified: 2019-06-28

__all__ = ["HeadQuarter"]

from .soldier import Dragon, Ninja, Iceman, Lion, Wolf

class HeadQuarter(object):

    INIT_ELEMENT = 0

    SOLDIER_ORDER = {
        'red':  (Iceman, Lion, Wolf, Ninja, Dragon),
        'blue': (Lion, Dragon, Ninja, Iceman, Wolf),
    }

    def __init__(self, name):
        self._name = name
        self._lose = False
        self._element = self.INIT_ELEMENT
        self._soldier_list = []
        self._soldier_count = {'dragon':0, 'ninja':0, 'iceman':0, 'lion':0, 'wolf':0}
        self._soldier_id = 0
        self._soldier_iter = self._soldier_generator(self.SOLDIER_ORDER[self._name])

    @property
    def name(self):
        return self._name

    @property
    def lose(self):
        return self._lose

    def __str__(self):
        return "%s %s" % (
                self._name,
                self.__class__.__name__.lower(),
            )

    def _soldier_generator(self, SOLDIERS):
        cnt = 0
        while True:
            for _Soldier in SOLDIERS:
                if self._element >= _Soldier.INIT_STRENGTH:
                    cnt = 0
                    self._soldier_id += 1
                    yield _Soldier(self, self._soldier_id)
            cnt += 1
            if cnt >=2:
                break

    def make_soldier(self, timer):
        if self._lose:
            return

        try:
            soldier = next(self._soldier_iter)
        except StopIteration:
            print("%s %s stops making warriors" % (timer, str(self)))
            self._lose = True
            return

        self._element -= soldier.INIT_STRENGTH
        self._soldier_list.append(soldier)
        self._soldier_count[soldier.type] += 1

        print("{timer} {soldier} born with strength {strength},{id} {type} in {headquarter}".format(
                timer=timer,
                soldier=soldier,
                strength=soldier.strength,
                id=self._soldier_count[soldier.type],
                type=soldier.type,
                headquarter=str(self),
            )
        )