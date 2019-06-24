from .weapon import Sword
from .weapon import Bomb
from .weapon import Arrow
from .weapon import get_weapon

class Soldier:
    def __init__(self, team, strength, id):
        self.team = team
        self.strength = strength
        self.id = id
        self.weapon_list = []
        self.remark = None

    def __str__(self):
        return self.team.name + ' ' + self.__class__.__name__.lower() + ' ' + str(self.id)

    def type_name(self):
        return self.__class__.__name__.lower()

class Dragon(Soldier):
    init_strength = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id)
        wp = get_weapon(id%3)
        self.morale = elem / self.init_strength - 1
        self.weapon_list.append(wp)
        self.remark = "It has a %s,and it's morale is %.2f"%(str(wp), self.morale)


class Ninja(Soldier):
    init_strength = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id)
        wp = get_weapon(id%3)
        self.weapon_list.append(wp)
        self.remark = "It has a " + str(wp)
        wp = get_weapon((id + 1)%3)
        self.weapon_list.append(wp)
        self.remark += " and a " + str(wp)

class Iceman(Soldier):
    init_strength = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id)
        wp = get_weapon(id%3)
        self.weapon_list.append(wp)
        self.remark = "It has a " + str(wp)
        
class Lion(Soldier):
    init_strength = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id)
        self.loyalty = elem - self.init_strength
        self.remark = "It's loyalty is %d"%(self.loyalty)


class Wolf(Soldier):
    init_strength = 0
    def __init__(self, team, id, elem):
        Soldier.__init__(self, team, self.init_strength, id)