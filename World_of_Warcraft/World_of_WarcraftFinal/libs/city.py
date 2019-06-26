# 战斗逻辑：
# 1. 第30分钟获取生命元顺便检查当前城市是否有两方武士，若是，则self.battle
#    打开，视为发生战斗，第3-5步只在self.battle开启时执行
# 2. 第35分钟时若有武士被射杀，则被射武士城市的self.shot_to_death打开，
#    跳过此后的第4步，直接进入第40分钟的战后清算阶段
# 3. 第38分钟直接处理战斗事件并修改双方士兵的生命与武器状态，输出暂时存到
#    self.info中，此后检查生命不大于0的士兵（至多一个）是否有炸弹，若有则
#    双方生命全部置0，清空self.info
# 4. 第40分钟战后清算阶段1，若有唯一存活士兵则接收奖励
# 5. 第40分钟战后清算阶段2，赚取生命元，更新旗帜，输出self.info 生命元事
#    件，旗帜事件，重置开关

class City:
    N = 0
    city_list = []
    def __init__(self, id):
        self.id = id
        self.Soldiers = {'red':[], 'blue':[]} # 其实最多每边只有一个
        self.battle = False
        self.shot_to_death = False
        self.info = {'red':None, 'blue':None, 'remark':None}
        self.flag = None
        self.element = 0
        self.winner = None
        self.last_winner = None
    
    def __str__(self):
        if self.id == 0:
            return 'red headquarter'
        elif self.id == City.N + 1:
            return 'blue headquarter'
        return 'city '+str(self.id)
    
    def print_info(self):
        if self.info['red'] != None:
            print(self.info['red'])
            self.info['red'] = None
        if self.info['blue'] != None:
            print(self.info['blue'])
            self.info['blue'] = None
        if self.info['remark'] != None:
            print(self.info['remark'])
            self.info['remark'] = None
    
    def clear_arrived_soldiers(self):
        if self.id == 0 and len(self.Soldiers['blue'])>0:
            self.Soldiers['blue'][0].erase()
        if self.id == City.N + 1 and len(self.Soldiers['red'])>0:
            self.Soldiers['red'][0].erase()
    
    def lion_escape(self, gametime):
        if len(self.Soldiers['red']) > 0 and hasattr(self.Soldiers['red'][0], 'do_escape'):
            self.Soldiers['red'][0].do_escape(gametime)
        if len(self.Soldiers['blue']) > 0 and hasattr(self.Soldiers['blue'][0], 'do_escape'):
            self.Soldiers['blue'][0].do_escape(gametime)

    def soldier_report(self, gametime, team):
        if len(self.Soldiers[team.name]) > 0:
            self.Soldiers[team.name][0].report_weapons(gametime)

    def do_spawn_elements(self):
        # 第20分钟的生成生命元
        self.element += 10

    def do_attain_elements(self, gametime):
        # 第30分钟的获取
        if len(self.Soldiers['red']) > 0 and len(self.Soldiers['blue']) > 0:
            self.battle = True
            return
        for pair in self.Soldiers.items():
            if len(pair[1])>0:
                pair[1][0].team.add_elements(self.element)
                print(gametime, pair[1][0], 'earned', self.element, 'elements for his headquarter')
                self.element = 0
                break
    
    def get_first(self):
        if self.flag == 'red':
            return 0
        elif self.flag == 'blue':
            return 1
        if self.id % 2 == 0:
            return 1 #blue
        else:
            return 0 #red

    def clear_info(self):
        self.info['red'] = None
        self.info['blue'] = None
        self.info['remark'] = None
    
    def do_shoot(self, gametime):
        if len(self.Soldiers['red'])>0 and len(City.city_list[self.id + 1].Soldiers['blue']) > 0:
            self.Soldiers['red'][0].shoot_arrow(City.city_list[self.id + 1].Soldiers['blue'][0], gametime)
        if len(self.Soldiers['blue'])>0 and len(City.city_list[self.id - 1].Soldiers['red']) > 0:
            self.Soldiers['blue'][0].shoot_arrow(City.city_list[self.id - 1].Soldiers['red'][0], gametime)
    
    def after_shoot(self):
        # 本来只有一个士兵的城市，士兵被射杀，直接清理
        if not self.battle:
            if len(self.Soldiers['red'])>0 and self.Soldiers['red'][0].strength <= 0:
                self.Soldiers['red'][0].erase()
            if len(self.Soldiers['blue'])>0 and self.Soldiers['blue'][0].strength <= 0:
                self.Soldiers['blue'][0].erase()

    
    def do_battle(self, gametime):
        if not self.battle:
            return
        actlist = [self.Soldiers['red'][0], self.Soldiers['blue'][0]]
        actlist[0].temp_hp = max(0, actlist[0].strength)
        actlist[1].temp_hp = max(0, actlist[1].strength)
        index = self.get_first()
        actlist[index].attack(actlist[index^1], gametime)
        actlist[index^1].attack(actlist[index], gametime, True)

        if ((actlist[0].strength<= 0 and actlist[0].weapon_dict['Bomb'] != None) \
            or (actlist[1].strength<= 0 and actlist[1].weapon_dict['Bomb'] != None)) \
            and not self.shot_to_death:
            if actlist[0].strength<= 0:
                index = 0
            else:
                index = 1
            actlist[0].strength = 0
            actlist[1].strength = 0
            print(gametime, actlist[index], 'used a bomb and killed', actlist[index^1])
            self.clear_info()
            return
        if actlist[0].strength<= 0 and actlist[1].strength> 0:
            self.winner = 'blue'
        elif actlist[0].strength> 0 and actlist[1].strength<= 0:
            self.winner = 'red'
        
    def do_send_elements(self, team):
        if self.winner != None and self.Soldiers[self.winner][0].team == team:
            if team.add_elements(-8):
                self.Soldiers[self.winner][0].strength += 8

    def after_war(self, gametime):
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
                    self.Soldiers['red'][0].yell(gametime, self)
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
                    self.Soldiers['blue'][0].yell(gametime, self)
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
        
        if self.element > 0:
            self.Soldiers[self.winner][0].team.add_elements(self.element)
            print(gametime, str(self.Soldiers[self.winner][0]), 'earned', self.element, \
                'elements for his headquarter')
            self.element = 0
        if self.winner == self.last_winner and self.winner != self.flag:
            self.flag = self.winner
            print(gametime, self.winner, 'flag raised in', self)
        self.last_winner = self.winner
        self.winner = None