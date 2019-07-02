#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: main.py
# modified: 2019-07-02

from libs.soldier import Dragon, Ninja, Iceman, Lion, Wolf
from libs.headquarter import HeadQuarter
from libs.city import City
from libs.weapon import Arrow
from libs.schedule import run

def main():

    #input_file = open('data/sample.txt', 'r')

    with open('data/input.txt', 'r') as _fin:

        fin = ( line.rstrip('\n') for line in _fin if line.strip() != '' )

        CASES = int(next(fin))
        for T in range(1, CASES+1):
            print("Case %d:" % T)

            HeadQuarter.INIT_ELEMENT, City.N, Arrow.R, Lion.K, TLE = map(int, next(fin).split())

            for _Soldier, strength, force in zip([Dragon, Ninja, Iceman, Lion, Wolf],
                                                 next(fin).split(),
                                                 next(fin).split()):
                _Soldier.INIT_STRENGTH = int(strength)
                _Soldier.INIT_FORCE = int(force)

            run(TLE)


if __name__ == '__main__':
    main()
