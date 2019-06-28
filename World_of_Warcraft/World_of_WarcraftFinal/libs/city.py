#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: city.py
# modified: 2019-06-28
'''
战斗逻辑：
1. 第30分钟获取生命元顺便检查当前城市是否有两方武士，若是，则self.battle
   打开，视为发生战斗，第3-5步只在self.battle开启时执行
2. 第35分钟时若有武士被射杀，则被射武士城市的self.shot_to_death打开，
   跳过此后的第4步，直接进入第40分钟的战后清算阶段
3. 第38分钟直接处理战斗事件并修改双方士兵的生命与武器状态，输出暂时存到
   self.info中，此后检查生命不大于0的士兵（至多一个）是否有炸弹，若有则
   双方生命全部置0，清空self.info
4. 第40分钟战后清算阶段1，若有唯一存活士兵则接收奖励
5. 第40分钟战后清算阶段2，赚取生命元，更新旗帜，输出self.info 生命元事
   件，旗帜事件，重置开关
'''

from .timer import timer

class City(object):

    N = 0
    city_list = []

    def __init__(self, id):
        self._id = id
        self.Soldiers = {'red':[], 'blue':[]} # 其实最多每边只有一个
        self.battle = False
        self.shot_to_death = False
        self.info = {}
        self.flag = None
        self._element = 0
        self.winner = None
        self.last_winner = None

    @property
    def id(self):
        return self._id

    @property
    def element(self):
        return self._element

    def __str__(self):
        if self._id == 0:
            return 'red headquarter'
        elif self._id == City.N + 1:
            return 'blue headquarter'
        return 'city %s' % self._id

    def print_info(self):
        for key in ('red','blue','remark'):
            if key in self.info:
                print(self.info.pop(key))

    def clear_arrived_soldiers(self):
        if self._id == 0 and len(self.Soldiers['blue'])>0:
            self.Soldiers['blue'][0].erase()
        if self._id == City.N + 1 and len(self.Soldiers['red'])>0:
            self.Soldiers['red'][0].erase()

    def lion_escape(self):
        from .soldier import Lion
        for color in ('red','blue'):
            soldiers = self.Soldiers[color]
            if len(soldiers) > 0 and isinstance(soldiers[0], Lion):
                soldiers[0].do_escape()

    def soldier_report(self, team):
        soldiers = self.Soldiers[team.name]
        if len(soldiers) > 0:
            soldiers[0].report_weapons()

    def do_spawn_elements(self):
        # 第20分钟的生成生命元
        self._element += 10

    def do_attain_elements(self):
        # 第30分钟的获取
        if all([ len(self.Soldiers[color]) > 0 for color in ('red','blue') ]):
            self.battle = True
            return
        for color, soldiers in self.Soldiers.items():
            if len(soldiers) > 0:
                soldier = soldiers[0]
                soldier.team.add_elements(self._element)
                print("%s %s earned %s elements for his headquarter" % (timer, soldier, self._element) )
                self._element = 0
                break

    def get_first(self):
        if self.flag is not None:
            return 0 if self.flag == 'red' else 1
        else:
            return (self._id + 1) % 2

    def do_shoot(self):
        for color, opcolor, step in [ ('red','blue',1), ('blue','red',-1) ]:
            soldiers = self.Soldiers[color]
            if len(soldiers) == 0:
                continue
            opsoldiers = City.city_list[self._id + step].Soldiers[opcolor]
            if all([ len(ss) > 0 for ss in (soldiers, opsoldiers) ]):
                soldiers[0].shoot_arrow(opsoldiers[0])

    def after_shoot(self):
        # 本来只有一个士兵的城市，士兵被射杀，直接清理
        if not self.battle:
            for color in ('red','blue'):
                soldiers = self.Soldiers[color]
                if len(soldiers) > 0 and soldiers[0].strength <= 0:
                    soldiers[0].erase()

    def do_battle(self):
        if not self.battle:
            return
        r1, b1 = actlist = [ self.Soldiers[color][0] for color in ('red','blue') ]
        for s in actlist:
            s.temp_hp = max(0, s.strength)

        idx = self.get_first()
        asd, fsd = actlist[idx], actlist[idx^1]
        asd.attack(fsd)
        fsd.attack(asd, True)

        if (any([ s.strength <= 0 and s.weapon_dict['Bomb'] is not None for s in actlist ])
            and not self.shot_to_death
            ):
            idx = 0 if r1.strength <= 0 else 1
            r1.strength = b1.strength = 0
            s1, s2 = actlist[idx], actlist[idx^1]
            print("%s %s used a bomb and killed %s" % (timer, s1, s2) )
            self.info.clear()
            return

        if r1.strength <= 0 and b1.strength > 0:
            self.winner = 'blue'
        elif r1.strength > 0 and b1.strength <= 0:
            self.winner = 'red'


    def do_send_elements(self, team):
        if self.winner is not None:
            ws = self.Soldiers[self.winner][0]
            if ws.team is team and team.add_elements(-8):
                ws.strength += 8


    def after_war(self):
        if not self.battle:
            return
        self.battle = False
        self.shot_to_death = False
        self.print_info()
        if self.Soldiers['red'][0].strength > 0:
            if hasattr(self.Soldiers['red'][0], 'yell'):
                if self.Soldiers['blue'][0].strength <= 0:
                    self.Soldiers['red'][0].morale += 0.2
                else:
                    self.Soldiers['red'][0].morale -= 0.2
                if self.get_first()==0:
                    self.Soldiers['red'][0].yell(self)
            if hasattr(self.Soldiers['blue'][0], 'loyalty'):
                self.Soldiers['blue'][0].lose_loyalty()
                if self.Soldiers['blue'][0].strength <= 0:
                    self.Soldiers['red'][0].strength += self.Soldiers['blue'][0].temp_hp
            if self.Soldiers['blue'][0].strength <= 0:
                self.Soldiers['blue'][0].was_stolen_weapons(self.Soldiers['red'][0])


        if self.Soldiers['blue'][0].strength > 0:
            if hasattr(self.Soldiers['blue'][0], 'yell'):
                if self.Soldiers['red'][0].strength <= 0:
                    self.Soldiers['blue'][0].morale += 0.2
                else:
                    self.Soldiers['blue'][0].morale -= 0.2
                if self.get_first()==1:
                    self.Soldiers['blue'][0].yell(self)
            if hasattr(self.Soldiers['red'][0], 'loyalty'):
                self.Soldiers['red'][0].lose_loyalty()
                if self.Soldiers['red'][0].strength <= 0:
                    self.Soldiers['blue'][0].strength += self.Soldiers['red'][0].temp_hp
            if self.Soldiers['red'][0].strength <= 0:
                self.Soldiers['red'][0].was_stolen_weapons(self.Soldiers['blue'][0])

        both_die = False
        if self.Soldiers['red'][0].strength <= 0:
            self.Soldiers['red'][0].erase()
            both_die = True
        if self.Soldiers['blue'][0].strength <= 0:
            self.Soldiers['blue'][0].erase()
            both_die = True

        if self.winner == None:
            # 这里逻辑不优雅
            if not both_die:
                self.last_winner = None #双活
            return

        if self._element > 0:
            self.Soldiers[self.winner][0].team.add_elements(self._element)
            print(timer, str(self.Soldiers[self.winner][0]), 'earned', self._element, \
                'elements for his headquarter')
            self._element = 0
        if self.winner == self.last_winner and self.winner != self.flag:
            self.flag = self.winner
            print(timer, self.winner, 'flag raised in', self)
        self.last_winner = self.winner
        self.winner = None