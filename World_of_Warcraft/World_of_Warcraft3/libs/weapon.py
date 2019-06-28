#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: weapon.py
# modified: 2019-06-28

__all__ = [

    "Weapon", "Sword", "Bomb", "Arrow",

    "WEAPONS",

    "battle_cmp",
    "stole_cmp",

]


class Weapon(object):

    def __str__(self):
        return self.__class__.__name__.lower()

class Sword(Weapon):
    wid = 0
    factor = 2

class Bomb(Weapon):
    wid = 1
    factor = 4

class Arrow(Weapon):
    wid = 2
    factor = 3
    def __init__(self):
        Weapon.__init__(self)
        self.number = 2

WEAPONS = (Sword, Bomb, Arrow)

def battle_cmp(wep1, wep2):
    if wep1.wid != wep2.wid:
        return wep1.wid - wep2.wid #编号小的优先
    elif wep1.wid == 2:
        return wep1.number - wep2.number #用过的优先
    else:
        return 0

def stole_cmp(wep1, wep2):
    if wep1.wid != wep2.wid:
        return wep1.wid - wep2.wid #编号小的优先
    elif wep1.wid == 2:
        return wep2.number - wep1.number #没用过的优先
    else:
        return 0