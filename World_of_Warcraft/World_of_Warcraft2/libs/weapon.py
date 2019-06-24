class Weapon:
    def __init__(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__.lower()
    
class Sword(Weapon):
    def __init__(self):
        Weapon.__init__(self)

class Bomb(Weapon):
    def __init__(self):
        Weapon.__init__(self)

class Arrow(Weapon):
    def __init__(self):
        Weapon.__init__(self)

weapon_tuple = Sword, Bomb, Arrow
def get_weapon(id):
    return weapon_tuple[id]()