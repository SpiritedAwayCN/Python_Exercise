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
    init_strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.init_strength, id)

class Ninja(Soldier):
    init_strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.init_strength, id)

class Iceman(Soldier):
    init_strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.init_strength, id)
        
class Lion(Soldier):
    init_strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.init_strength, id)

class Wolf(Soldier):
    init_strength = 0
    def __init__(self, team, id):
        Soldier.__init__(self, team, self.init_strength, id)