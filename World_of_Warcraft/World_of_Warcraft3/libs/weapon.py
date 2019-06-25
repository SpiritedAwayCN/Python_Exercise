class Weapon:
    def __init__(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__.lower()
    
class Sword(Weapon):
    wid = 0
    factor = 2
    def __init__(self):
        Weapon.__init__(self)

class Bomb(Weapon):
    wid = 1
    factor = 4
    def __init__(self):
        Weapon.__init__(self)

class Arrow(Weapon):
    wid = 2
    factor = 3
    def __init__(self):
        Weapon.__init__(self)
        self.number = 2

weapon_tuple = Sword, Bomb, Arrow
def get_weapon(id):
    return weapon_tuple[id]()

def battle_cmp(wep1, wep2):
    if wep1.wid != wep2.wid:
        return wep1.wid - wep2.wid #编号小的优先
    elif wep1.wid == 2:
        return wep1.number - wep2.number #用过的优先
    else:
        return 0

def stole_cmp(wep1, wep2):
    if wep1.wid != wep2.wid:
        return wep1.wid - wep2.wid #编号小的优先
    elif wep1.wid == 2:
        return wep2.number - wep1.number #没用过的优先
    else:
        return 0