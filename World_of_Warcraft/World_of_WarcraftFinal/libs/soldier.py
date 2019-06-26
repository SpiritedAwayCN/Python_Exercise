from .weapon import Sword
from .weapon import Bomb
from .weapon import Arrow
from .weapon import get_weapon
from .city import City
import copy

class Soldier:
    def __init__(self, team, strength, id, force):
        self.team = team
        self.strength = strength
        self.id = id
        self.weapon_dict = {'Sword':None, 'Bomb':None, 'Arrow':None}
        self.remark = None
        self.force = force
        self.__weapon_index = 0
        self.temp_hp = 0
        if team.name == 'red':
            self.city = City.city_list[0]
        else:
            self.city = City.city_list[City.N + 1]
        self.city.Soldiers[team.name].append(self)

    def __str__(self):
        return self.team.name + ' ' + self.__class__.__name__.lower() + ' ' + str(self.id)

    def type_name(self):
        return self.__class__.__name__.lower()
    
    def march_next(self, gametime, opteam):
        cid = self.city.id
        vstr = ' marched to '
        if self.team.name == 'red':
            self.city = City.city_list[cid + 1]
        else:
            self.city = City.city_list[cid - 1]
        self.city.Soldiers[self.team.name].append(self)
        if self.city.id == 0 or self.city.id == City.N + 1:
            # 到达终点的在输出信息时再删
            opteam.enemies.append(self)
            vstr = ' reached '
            if len(opteam.enemies) > 1:
                self.city.info['remark'] = str(gametime) + ' ' + str(opteam) + ' was taken'
        
        if isinstance(self, Iceman):
            self.step_count += 1
            if self.step_count % 2 == 0:
                self.strength = max(self.strength - 9, 1)
                self.force += 20
        self.city.info[self.team.name] = str(gametime) + ' ' + \
            str(self) + vstr + str(self.city) + \
            ' with {:d} elements and force {:d}'.format(self.strength, self.force)
        City.city_list[cid].Soldiers[self.team.name].remove(self)

    def report_weapons(self, gametime):
        cnt = 0
        wep_str = ''
        if self.weapon_dict['Arrow'] != None:
            wep_str += str(self.weapon_dict['Arrow'])
            cnt += 1
        if self.weapon_dict['Bomb'] != None:
            if cnt > 0:
                wep_str += ','
            wep_str += str(self.weapon_dict['Bomb'])
            cnt += 1
        if self.weapon_dict['Sword'] != None:
            if cnt > 0:
                wep_str += ','
            wep_str += str(self.weapon_dict['Sword'])
            cnt += 1
        if cnt == 0:
            wep_str = 'no weapon'
        print(gametime, self, 'has', wep_str)
        

    def was_stolen_weapons(self, source):
        if not isinstance(source, Wolf):
            return
        for wep_pair in self.weapon_dict.items():
            if wep_pair[1] != None and source.weapon_dict[wep_pair[0]] == None:
                source.weapon_dict[wep_pair[0]] = wep_pair[1]
    
    def attack(self, target, gametime, fight_back = False):
        # 38分钟时直接attack，若有自爆直接没，若无自爆第40分钟直接输出战斗结果
        if self.strength <= 0 or target.strength <= 0:
            return
        if fight_back and isinstance(self, Ninja):
            return
        temptime = copy.copy(gametime)
        temptime.minute = 40
        vstr = ' attacked '
        damage = self.force
        if fight_back:
            vstr = ' fought back against '
            damage //= 2
        if self.weapon_dict['Sword'] != None:
            damage += self.weapon_dict['Sword'].atk
            self.weapon_dict['Sword'].atk *= 8
            self.weapon_dict['Sword'].atk //= 10
            if self.weapon_dict['Sword'].atk == 0:
                self.weapon_dict['Sword'] = None
        target.strength -= damage
        if not fight_back:
            self.city.info['red'] = str(temptime) + ' ' + str(self) + \
                vstr + str(target) + ' in ' + str(self.city) + ' with %d elements and force %d'%(self.strength, self.force)
        else:
            self.city.info['blue'] = str(temptime) + ' ' + str(self) + \
                vstr + str(target) + ' in ' + str(self.city)
        if target.strength <= 0:
            self.city.info['remark'] = str(temptime) + ' ' + str(target) + \
                ' was killed in ' + str(self.city)
    
    def shoot_arrow(self, target, gametime):
        if self.weapon_dict['Arrow'] == None:
            return
        target.strength -= Arrow.R
        self.weapon_dict['Arrow'].number -= 1
        if self.weapon_dict['Arrow'].number == 0:
            self.weapon_dict['Arrow'] = None
        if target.strength <= 0:
            print(gametime, self, 'shot and killed', target)
            if target.city.battle == True:
                target.city.shot_to_death = True
        else:
            print(gametime, self, 'shot')
    
    def check_weapon(self):
        if self.weapon_dict['Sword'] != None and self.weapon_dict['Sword'].atk == 0:
            self.weapon_dict['Sword'] = None

    def erase(self):
        self.city.Soldiers[self.team.name].remove(self)
        self.team.soldier_list.remove(self)

class Dragon(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        wp = get_weapon(id%3, self.init_force // 5)
        self.morale = elem / self.init_strength - 1
        self.weapon_dict[wp.__class__.__name__] = wp
        self.remark = "Its morale is %.2f"%(self.morale)
        self.check_weapon()
    def yell(self, gametime, city):
        if self.morale > 0.8:
            print(gametime, self, 'yelled in', city)

class Ninja(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        wp = get_weapon(id%3, self.init_force // 5)
        self.weapon_dict[wp.__class__.__name__] = wp
        wp = get_weapon((id + 1)%3, self.init_force // 5)
        self.weapon_dict[wp.__class__.__name__] = wp
        self.check_weapon()

class Iceman(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        wp = get_weapon(id%3, self.init_force // 5)
        self.weapon_dict[wp.__class__.__name__] = wp
        self.step_count = 0
        self.check_weapon()
        
class Lion(Soldier):
    K = 0
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        self.loyalty = elem - self.init_strength
        self.remark = "Its loyalty is %d"%(self.loyalty)
    def lose_loyalty(self):
        self.loyalty -= Lion.K
    def do_escape(self, gametime):
        if self.loyalty <= 0:
            print(gametime, self, 'ran away')
            self.erase()

class Wolf(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)