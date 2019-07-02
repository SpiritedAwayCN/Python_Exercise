#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: weapon.py
# modified: 2019-07-02

__all__ = ["Sword","Bomb","Arrow"]

class Weapon:

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name.lower()


class Sword(Weapon):

    wid = 0

    def __init__(self, atk):
        self.atk = atk

    def __str__(self):
        return 'sword(%d)' % self.atk


class Bomb(Weapon):

    wid = 1

    def __init__(self, atk):
        pass


class Arrow(Weapon):

    wid = 2
    R = 0

    def __init__(self, atk):
        self.number = 3

    def __str__(self):
        return 'arrow(%d)' % self.number


_WEAPONS = Sword, Bomb, Arrow

def get_weapon(id_, atk):
    return _WEAPONS[id_](atk)