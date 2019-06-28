#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: main.py
# modified: 2019-06-28

from libs.soldier import Dragon, Ninja, Iceman, Lion, Wolf
from libs.headquarter import HeadQuarter
from libs.schedule import run


def main():
    # fin = open('data/sample.txt', 'r')

    with open('data/input.txt','r') as fin:

        CASES = int(fin.readline())

        for T in range(1, CASES+1):

            print("Case:%d" % T)

            HeadQuarter.INIT_ELEMENT = int(fin.readline())

            for _Soldier, strength in zip( [Dragon, Ninja, Iceman, Lion, Wolf],
                                           fin.readline().split() ):
                _Soldier.INIT_STRENGTH = int(strength)

            run()


if __name__ == '__main__':
    main()