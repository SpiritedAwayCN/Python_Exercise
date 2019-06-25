from .weapon import Sword
from .weapon import Bomb
from .weapon import Arrow
from .weapon import get_weapon
from .weapon import battle_cmp
from .weapon import stole_cmp
from functools import cmp_to_key
from .city import City

class Soldier:
    def __init__(self, team, strength, id, force):
        self.team = team
        self.strength = strength
        self.id = id
        self.weapon_list = []
        self.remark = None
        self.force = force
        self.__weapon_index = 0
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
            opteam.enemy_count += 1
            vstr = ' reached '
            self.city.info['remark'] = str(gametime) + ' ' + str(opteam) + ' was taken'
        
        if isinstance(self, Lion):
            self.loyalty -= Lion.K
        elif isinstance(self, Iceman):
            self.strength -= self.strength // 10
        self.city.info[self.team.name] = str(gametime) + ' ' + \
            str(self) + vstr + str(self.city) + \
            ' with {:d} elements and force {:d}'.format(self.strength, self.force)
        City.city_list[cid].Soldiers[self.team.name].remove(self)

    def report_weapons(self, gametime):
        count_list = [0, 0, 0]
        for wep in self.weapon_list:
            count_list[wep.wid] += 1
        print(gametime, self, 'has', count_list[0], 'sword', \
                count_list[1], 'bomb', count_list[2], 'arrow and', \
                self.strength, 'elements')
        

    def was_stolen_weapons(self, source, gametime, city ,stolen = False):
        if stolen and isinstance(self, Wolf):
            return
        if stolen and not isinstance(source, Wolf):
            return
        if len(self.weapon_list) == 0:
            return
        cnt = 0
        self.weapon_list.sort(key = cmp_to_key(stole_cmp), reverse = True)
        # 没用deque, 直接反向排提高pop效率
        min_wep = self.weapon_list[len(self.weapon_list) - 1]
        while len(source.weapon_list) < 10 and len(self.weapon_list) > 0:
            wep = self.weapon_list[len(self.weapon_list) - 1]
            if stolen and wep.wid != min_wep.wid:
                break # wolf只抢一种编号
            self.weapon_list.pop()
            cnt += 1
            source.weapon_list.append(wep)
        if cnt > 0 and stolen:
            print(gametime, source, 'took', cnt, min_wep, \
                'from', self, 'in', city)

    def prepare_weapon(self):
        self.weapon_list.sort(key = cmp_to_key(battle_cmp))
        self.__weapon_index = 0

    def isInvalidAttack(self):
        if len(self.weapon_list) == 0:
            return True
        if self.weapon_list[len(self.weapon_list) - 1].wid == 0 \
            and self.force * Sword.factor // 10 == 0:
            return True  #武器不再变化时，只剩剑，由于已排序，只看最后一个是否是剑
        return False
    
    def attack(self, target):
        if len(self.weapon_list) == 0:
            return
        wep = self.weapon_list[self.__weapon_index]
        target.strength -= self.force * wep.factor // 10
        if wep.wid == 1: #bomb
            self.weapon_list.pop(self.__weapon_index)
            if not isinstance(self, Ninja):
                self.strength -= (self.force * wep.factor // 10) // 2
        elif wep.wid == 2: #arrow
            wep.number -= 1
            if wep.number <= 0:
                self.weapon_list.pop(self.__weapon_index)
        if len(self.weapon_list) != 0:
            self.__weapon_index = (self.__weapon_index + 1) % len(self.weapon_list)

    def erase(self):
        self.city.Soldiers[self.team.name].remove(self)
        self.team.soldier_list.remove(self)

class Dragon(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        wp = get_weapon(id%3)
        self.morale = elem / self.init_strength - 1
        self.weapon_list.append(wp)
        #self.remark = "It has a %s,and it's morale is %.2f"%(str(wp), self.morale)
    def yell(self, gametime, city):
        print(gametime, self, 'yelled in', city)



class Ninja(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        wp = get_weapon(id%3)
        self.weapon_list.append(wp)
        wp = get_weapon((id + 1)%3)
        self.weapon_list.append(wp)

class Iceman(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        wp = get_weapon(id%3)
        self.weapon_list.append(wp)
        
class Lion(Soldier):
    K = 0
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)
        wp = get_weapon(id%3)
        self.weapon_list.append(wp)
        self.loyalty = elem - self.init_strength
        self.remark = "Its loyalty is %d"%(self.loyalty)
    
    def do_escape(self, gametime):
        if self.loyalty <= 0:
            print(gametime, self, 'ran away')
            self.erase()

class Wolf(Soldier):
    init_strength = 0
    init_force = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id, self.init_force)