#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: soldier.py
# modified: 2019-06-28

__all__ = ["Dragon", "Ninja", "Iceman", "Lion", "Wolf"]


class Soldier(object):

    INIT_STRENGTH = -1  # 基类也最好申明一下

    def __init__(self, team, strength, id_):
        self._team = team
        self.strength = strength
        self._id = id_

    @property
    def team(self):
        return self._team

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self.__class__.__name__.lower()

    def __str__(self):
        return "%s %s %s" % (self._team.name, self.type, self._id)


class Dragon(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_):
        super().__init__(team, self.INIT_STRENGTH, id_)

class Ninja(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_):
        super().__init__(team, self.INIT_STRENGTH, id_)

class Iceman(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_):
        super().__init__(team, self.INIT_STRENGTH, id_)

class Lion(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_):
        super().__init__(team, self.INIT_STRENGTH, id_)

class Wolf(Soldier):

    INIT_STRENGTH = 0

    def __init__(self, team, id_):
        super().__init__(team, self.INIT_STRENGTH, id_)