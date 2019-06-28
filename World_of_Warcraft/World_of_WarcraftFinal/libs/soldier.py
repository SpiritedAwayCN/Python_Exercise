#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: soldier.py
# modified: 2019-06-28

__all__ = ["Dragon", "Ninja", "Iceman", "Lion", "Wolf"]

from .timer import timer
from .weapon import Sword, Bomb, Arrow, get_weapon
from .city import City
import copy

class Soldier(object):

    INIT_STRENGTH = -1
    INIT_FORCE = -1

    def __init__(self, team, strength, id_, force):
        self._team = team
        self._strength = strength
        self._id = id_
        self.weapon_dict = {'Sword':None, 'Bomb':None, 'Arrow':None}
        self._remark = None
        self._force = force
        self.temp_hp = 0
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

    @strength.setter
    def strength(self, strength):
        self._strength = strength

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
            opteam.enemies.append(self)
            vstr = 'reached'
            if len(opteam.enemies) > 1:
                self._city.info['remark'] = "%s %s was taken" % (timer, opteam)

        if isinstance(self, Iceman):
            self._step_count += 1
            if self._step_count % 2 == 0:
                self._strength = max(self._strength - 9, 1)
                self._force += 20

        self._city.info[self._team.name] = "%s %s %s %s with %d elements and force %d" % (
                                                timer, str(self), vstr, str(self._city),
                                                self._strength, self._force,
                                            )

        City.city_list[cid].Soldiers[self._team.name].remove(self)


    def report_weapons(self):
        cnt = 0
        wep_str = ''
        for wpname in ('Arrow','Bomb','Sword'):
            if self.weapon_dict[wpname] is not None:
                if cnt > 0:
                    wep_str += ','
                wep_str += str(self.weapon_dict[wpname])
                cnt += 1
        if cnt == 0:
            wep_str = 'no weapon'
        print("%s %s has %s" % (timer, self, wep_str) )


    def was_stolen_weapons(self, source):
        if not isinstance(source, Wolf):
            return
        for name, wp in self.weapon_dict.items():
            if wp is not None and source.weapon_dict[name] is None:
                source.weapon_dict[name] = wp


    def attack(self, target, fight_back=False):
        # 38分钟时直接attack，若有自爆直接没，若无自爆第40分钟直接输出战斗结果
        if any([ s.strength <= 0 for s in (self, target) ]):
            return
        if fight_back and isinstance(self, Ninja):
            return

        _timer = copy.copy(timer)
        _timer.minute = 40

        vstr = 'attacked' if not fight_back else 'fought back against'

        damage = self._force
        if fight_back:
            damage //= 2

        if self.weapon_dict['Sword'] is not None:
            sw = self.weapon_dict['Sword']
            damage += sw.atk
            sw.atk *= 8
            sw.atk //= 10
            if sw.atk == 0:
                self.weapon_dict['Sword'] = None  # 这里必须要对 dict 赋值

        target.strength -= damage
        if not fight_back:
            self._city.info['red'] = "%s %s %s %s in %s with %d elements and force %d" % (
                                        _timer, str(self), vstr, str(target), str(self._city),
                                        self._strength, self._force,
                                    )
        else:
            self._city.info['blue'] = "%s %s %s %s in %s" % (_timer, self, vstr, target, self._city)

        if target.strength <= 0:
            self._city.info['remark'] = "%s %s was killed in %s" % (_timer, target, self._city)


    def shoot_arrow(self, target):
        if self.weapon_dict['Arrow'] is None:
            return

        arw = self.weapon_dict['Arrow']
        arw.number -= 1
        if arw.number == 0:
            self.weapon_dict['Arrow'] = None

        target.strength -= Arrow.R
        if target.strength <= 0:
            print("%s %s shot and killed %s" % (timer, self, target) )

            if target.city.battle:
                target.city.shot_to_death = True
        else:
            print("%s %s shot" % (timer, self) )

    def check_weapon(self):
        sw = self.weapon_dict.get('Sword')
        if sw is not None and sw.atk == 0:
            self.weapon_dict['Sword'] = None

    def erase(self):
        self._city.Soldiers[self._team.name].remove(self)
        self._team.soldiers.remove(self)


class Dragon(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        wp = get_weapon( self._id % 3, self.INIT_FORCE // 5 )
        self._morale = elem / self.INIT_STRENGTH - 1
        self.weapon_dict[wp.name] = wp
        self._remark = "Its morale is %.2f" % self._morale
        self.check_weapon()

    @property
    def morale(self):
        return self._morale

    @morale.setter
    def morale(self, morale):
        self._morale = morale

    def yell(self, city):
        if self._morale > 0.8:
            print("%s %s yelled in %s" % (timer, self, city) )


class Ninja(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        wp1 = get_weapon( self._id % 3, self.INIT_FORCE // 5 )
        wp2 = get_weapon( (self._id + 1) % 3, self.INIT_FORCE // 5 )
        self.weapon_dict[wp1.name] = wp1
        self.weapon_dict[wp2.name] = wp2
        self.check_weapon()


class Iceman(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        wp = get_weapon( self._id % 3, self.INIT_FORCE // 5 )
        self.weapon_dict[wp.name] = wp
        self._step_count = 0
        self.check_weapon()


class Lion(Soldier):

    K = 0
    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)
        self._loyalty = elem - self.INIT_STRENGTH
        self._remark = "Its loyalty is %d" % self._loyalty

    @property
    def loyalty(self):
        return self._loyalty

    def lose_loyalty(self):
        self._loyalty -= Lion.K

    def do_escape(self):
        if self._loyalty <= 0:
            print("%s %s ran away" % (timer, self) )
            self.erase()


class Wolf(Soldier):

    INIT_STRENGTH = 0
    INIT_FORCE = 0

    def __init__(self, team, id_, elem):
        super().__init__(team, self.INIT_STRENGTH, id_, self.INIT_FORCE)