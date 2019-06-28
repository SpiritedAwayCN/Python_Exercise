#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: weapon.py
# modified: 2019-06-28

__all__= [

    "Sword", "Bomb", "Arrow",
    "WEAPONS",

]


class Weapon(object):

    def __str__(self):
        return self.__class__.__name__.lower()

class Sword(Weapon):
    pass

class Bomb(Weapon):
    pass

class Arrow(Weapon):
    pass


WEAPONS = (Sword, Bomb, Arrow)
