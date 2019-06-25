class City:
    N = 0
    city_list = []
    def __init__(self, id):
        self.id = id
        self.Soldiers = {'red':[], 'blue':[]}
        # 其实最多每边只有一个
        self.info = {'red':None, 'blue':None, 'remark':None}
    
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

    def soldier_report(self, gametime):
        if len(self.Soldiers['red']) > 0:
            self.Soldiers['red'][0].report_weapons(gametime)
        if len(self.Soldiers['blue']) > 0:
            self.Soldiers['blue'][0].report_weapons(gametime)
    
    def do_stole_weapons(self, gametime):
        if len(self.Soldiers['red']) > 0 and len(self.Soldiers['blue']) > 0:
            self.Soldiers['red'][0].was_stolen_weapons(self.Soldiers['blue'][0], gametime, self, True)
            self.Soldiers['blue'][0].was_stolen_weapons(self.Soldiers['red'][0], gametime, self, True)
    
    def get_first(self):
        if self.id % 2 == 0:
            return 1 #blue
        else:
            return 0 #red
    
    def do_battle(self, gametime):
        if len(self.Soldiers['red']) == 0 or len(self.Soldiers['blue']) == 0:
            return
        act_list = [self.Soldiers['red'][0], self.Soldiers['blue'][0]]
        index = self.get_first()
        
        while True:
            if act_list[0].isInvalidAttack() and act_list[1].isInvalidAttack():
                print(gametime, 'both', act_list[0],'and',act_list[1], 'were alive in', self)
                for i in range(2):
                    if hasattr(act_list[i], 'yell'):
                        act_list[i].yell(gametime, self)
                break
            act_list[index].attack(act_list[index ^ 1])
            if act_list[0].strength <= 0 and act_list[1].strength <= 0:
                print(gametime, 'both', act_list[0], 'and', act_list[1], \
                    'died in', self)
                act_list[0].erase()
                act_list[1].erase()
                break
            if act_list[0].strength > 0 and act_list[1].strength > 0:
                index ^= 1
                continue
            if act_list[0].strength > 0:
                winner_index = 0
            else:
                winner_index = 1
            act_list[winner_index ^ 1].was_stolen_weapons(act_list[winner_index], gametime, self)
            print(gametime, act_list[winner_index], 'killed', act_list[winner_index ^ 1], \
                'in', self, 'remaining %d elements'%act_list[winner_index].strength)
            act_list[winner_index ^ 1].erase()
            if hasattr(act_list[winner_index], 'yell'):
                act_list[winner_index].yell(gametime, self)
            break
