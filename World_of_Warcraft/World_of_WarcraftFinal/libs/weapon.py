class Weapon:
    def __init__(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__.lower()
    
class Sword(Weapon):
    wid = 0
    def __init__(self, atk):
        Weapon.__init__(self)
        self.atk = atk
    def __str__(self):
        return 'sword(%d)'%self.atk

class Bomb(Weapon):
    wid = 1
    def __init__(self, atk):
        Weapon.__init__(self)

class Arrow(Weapon):
    wid = 2
    R = 0
    def __init__(self, atk):
        Weapon.__init__(self)
        self.number = 3
    def __str__(self):
        return 'arrow(%d)'%self.number

weapon_tuple = Sword, Bomb, Arrow
def get_weapon(id, atk):
    return weapon_tuple[id](atk)