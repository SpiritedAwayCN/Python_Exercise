#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: city.py
# modified: 2019-06-28

__all__ = ["City"]

from .timer import timer

class City(object):

    N = 0
    city_list = []

    def __init__(self, id_):
        self._id = id_
        self.Soldiers = {'red':[], 'blue':[]} # 这个写法是正确的，不可以 dict.fromkeys(['red','blue'], []) 具体看 '深浅拷贝'
        # 其实最多每边只有一个
        # self.info = dict.fromkeys(['red','blue','remark'])
        self.info = {}

    @property
    def id(self):
        return self._id

    def __str__(self):
        if self._id == 0:
            return 'red headquarter'
        elif self._id == City.N + 1:
            return 'blue headquarter'
        else:
            return 'city %s' % self._id

    def print_info(self):
        for key in ('red','blue','remark'):
            if key in self.info:
                print(self.info.pop(key))

    def clear_arrived_soldiers(self):
        for _id, color in [ (City.N+1, 'red'), (0, 'blue') ]:
            soldiers = self.Soldiers[color]
            if self._id == _id and len(soldiers) > 0:
                soldiers[0].erase()

    def lion_escape(self):
        from .soldier import Lion  # 局部 import 避免循环 import
        for color in ('red','blue'):
            soldiers = self.Soldiers[color]
            if len(soldiers) > 0 and isinstance(soldiers[0], Lion):
                soldiers[0].do_escape()

    def soldier_report(self):
        for color in ('red','blue'):
            soldiers = self.Soldiers[color]
            if len(soldiers) > 0:
                soldiers[0].report_weapons()

    def do_stole_weapons(self):
        r1, b1 = [
            soldiers[0] if len(soldiers) > 0 else None
            for soldiers in [ self.Soldiers[color] for color in ('red','blue') ]
        ]
        # if all([r1, b1]): # 这个写法本质上还是用 == True 来判断，对于 None 来说是不规范的
        if r1 is not None and b1 is not None:
            r1.was_stolen_weapons(b1, self, True)
            b1.was_stolen_weapons(r1, self, True)

    def get_first(self):
        # return 1 if self._id % 2 == 0 else 0
        return (self._id + 1) % 2

    def do_battle(self):
        from .soldier import Dragon # 局部 import

        if any([ len(self.Soldiers[color]) == 0 for color in ('red','blue') ]):
            return

        sList = [ self.Soldiers[color][0] for color in ('red','blue') ]
        idx = self.get_first()

        while True:

            if all([ s.is_invalid_attack() for s in sList ]):
                print("%s both %s and %s were alive in %s" % (timer, *sList, self))
                for s in sList:
                    if isinstance(s, Dragon):
                        s.yell(self)
                break

            sList[idx].attack(sList[idx ^ 1])
            if all([ s.strength <= 0 for s in sList ]):
                print("%s both %s and %s died in %s" % (timer, *sList, self))
                for s in sList:
                    s.erase()
                break

            if all([ s.strength > 0 for s in sList ]):
                idx ^= 1
                continue

            widx = 0 if sList[0].strength > 0 else 1
            ws, ls = sList[widx], sList[widx ^ 1]

            ls.was_stolen_weapons(ws, self)

            print("%s %s killed %s in %s remaining %d elements" % (
                    timer, ws, ls, str(self), ws.strength,
                )
            )

            ls.erase()

            if isinstance(ws, Dragon):
                ws.yell(self)

            break
