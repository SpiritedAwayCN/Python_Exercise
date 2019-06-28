#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: soldier.py
# modified: 2019-06-28

__all__ = ["Soldier"]

from .weapon import WEAPONS

class Soldier(object):

    INIT_STRENGTH = -1

    def __init__(self, team, strength, id_):
        self._team = team
        self.strength = strength
        self._id = id_
        self._weapon_list = []
        self._remark = None

    @property
    def type(self):
        return self.__class__.__name__.lower()

    @property
    def team(self):
        return self._team

    @property
    def id(self):
        return self._id

    @property
    def remark(self):
        return self._remark

    def __str__(self):
        return "%s %s %s" % (self._team.name, self.type, self._id)


class Dragon(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_)
        wp = WEAPONS[self._id % 3]()
        self._morale = elem / self.INIT_STRENGTH - 1
        self._weapon_list.append(wp)
        self._remark = "It has a %s,and it's morale is %.2f" % (str(wp), self._morale)

    @property
    def morale(self):
        return self._morale


class Ninja(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_)
        wp1 = WEAPONS[self._id % 3]()
        wp2 = WEAPONS[(self._id + 1)%3]()
        self._weapon_list.extend([wp1, wp2])
        self._remark = "It has a %s and a %s" % (str(wp1), str(wp2))

class Iceman(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_)
        wp = WEAPONS[self._id % 3]()
        self._weapon_list.append(wp)
        self._remark = "It has a %s" % str(wp)

class Lion(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_)
        self._loyalty = elem - self.INIT_STRENGTH
        self._remark = "It's loyalty is %d" % self._loyalty

    @property
    def loyalty(self):
        return self._loyalty


class Wolf(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_)