class Soldier:
    def __init__(self, team, strength, id):
        self.team = team
        self.strength = strength
        self.id = id

    def __str__(self):
        return self.team.name + ' ' + self.__class__.__name__.lower() + ' ' + str(self.id)

    def type_name(self):
        return self.__class__.__name__.lower()

class Dragon(Soldier):
    strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.strength, id)

class Ninja(Soldier):
    strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.strength, id)

class Iceman(Soldier):
    strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.strength, id)
        
class Lion(Soldier):
    strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.strength, id)

class Wolf(Soldier):
    strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.strength, id)