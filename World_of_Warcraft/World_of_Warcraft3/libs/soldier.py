#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: soldier.py
# modified: 2019-06-28

__all__ = ["Dragon", "Ninja", "Iceman", "Lion", "Wolf"]

from functools import cmp_to_key
from .timer import timer
from .weapon import Sword, Bomb, Arrow, WEAPONS, battle_cmp, stole_cmp
from .city import City


class Soldier(object):

    INIT_STRENGTH = -1
    INIT_FORCE = -1

    def __init__(self, team, strength, id_, force):
        self._team = team
        self._strength = strength
        self._id = id_
        self._wp_list = []
        self._remark = None
        self._force = force
        self._wp_idx = 0
        self._city = City.city_list[ 0 if team.name == 'red' else City.N+1 ]
        self._city.Soldiers[team.name].append(self)

    @property
    def type(self):
        return self.__class__.__name__.lower()

    @property
    def team(self):
        return self._team

    @property
    def city(self):
        return self._city

    @property
    def id(self):
        return self._id

    @property
    def remark(self):
        return self._remark

    @property
    def strength(self):
        return self._strength

    @property
    def force(self):
        return self._force

    def __str__(self):
        return "%s %s %s" % (self._team.name, self.type, self._id)

    def march_next(self, opteam):
        cid = self._city.id
        vstr = 'marched to'
        self._city = City.city_list[ cid+1 if self._team.name == 'red' else cid-1 ]
        self._city.Soldiers[self._team.name].append(self)
        if self._city.id in (0, City.N+1):
            # 到达终点的在输出信息时再删
            opteam.add_enemy_count()
            vstr = 'reached'
            self._city.info['remark'] = "%s %s was taken" % (timer, opteam)

        if isinstance(self, Lion):
            self._loyalty -= Lion.K
        elif isinstance(self, Iceman):
            self._strength -= self._strength // 10
        self._city.info[self._team.name] = "%s %s %s %s with %d elements and force %d" % (
                                            timer, str(self), vstr, str(self._city),
                                            self._strength, self._force
                                        )

        City.city_list[cid].Soldiers[self._team.name].remove(self)

    def report_weapons(self):
        cnts = [0, 0, 0]
        for wep in self._wp_list:
            cnts[wep.wid] += 1
        print("%s %s has %s sword %s bomb %s arrow and %s elements" % (
                timer, str(self), *cnts, self._strength,
            )
        )

    def was_stolen_weapons(self, source, city, stolen=False):
        if stolen and ( isinstance(self, Wolf) or not isinstance(source, Wolf) ):
            return
        if len(self._wp_list) == 0:
            return

        cnt = 0
        self._wp_list.sort(key=cmp_to_key(stole_cmp), reverse=True)
        # 没用deque, 直接反向排提高pop效率
        min_wep = self._wp_list[-1]

        while len(source._wp_list) < 10 and len(self._wp_list) > 0:
            wep = self._wp_list[-1]
            if stolen and wep.wid != min_wep.wid:
                break # wolf只抢一种编号
            self._wp_list.pop()
            cnt += 1
            source._wp_list.append(wep)

        if stolen and cnt > 0:
            print("%s %s took %s %s from %s in %s" % (
                    timer, source, cnt, min_wep, str(self), city,
                )
            )

    def prepare_weapon(self):
        self._wp_list.sort(key=cmp_to_key(battle_cmp))
        self._wp_idx = 0

    def is_invalid_attack(self):
        if len(self._wp_list) == 0:
            return True
        if (self._wp_list[-1].wid == 0
            and self._force * Sword.factor // 10 == 0
            ):
            return True  #武器不再变化时，只剩剑，由于已排序，只看最后一个是否是剑
        return False

    def attack(self, target):
        if len(self._wp_list) == 0:
            return

        wep = self._wp_list[self._wp_idx]
        target._strength -= self._force * wep.factor // 10

        if isinstance(wep, Bomb):
            self._wp_list.pop(self._wp_idx)
            if not isinstance(self, Ninja):
                self._strength -= (self._force * wep.factor // 10) // 2

        elif isinstance(wep, Arrow):
            wep.number -= 1
            if wep.number <= 0:
                self._wp_list.pop(self._wp_idx)

        if len(self._wp_list) > 0:
            self._wp_idx = (self._wp_idx + 1) % len(self._wp_list)

    def erase(self):
        self._city.Soldiers[self._team.name].remove(self)
        self._team.soldiers.remove(self)


class Dragon(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        wp = WEAPONS[self._id % 3]()
        self._morale = elem / self.INIT_STRENGTH - 1
        self._wp_list.append(wp)

    @property
    def morale(self):
        return self._morale

    def yell(self, city):
        print("%s %s yelled in %s" % (timer, self, city))


class Ninja(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        wp1 = WEAPONS[self._id % 3]()
        wp2 = WEAPONS[(self._id + 1) % 3]()
        self._wp_list.extend([wp1, wp2])


class Iceman(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        wp = WEAPONS[self._id % 3]()
        self._wp_list.append(wp)


class Lion(Soldier):

    K = 0
    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        wp = WEAPONS[self._id % 3]()
        self._wp_list.append(wp)
        self._loyalty = elem - self.INIT_STRENGTH
        self._remark = "Its loyalty is %d" % (self._loyalty)

    @property
    def loyalty(self):
        return self._loyalty

    def do_escape(self):
        if self._loyalty <= 0:
            print("%s %s ran away" % (timer, str(self)) )
            self.erase()


class Wolf(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)