from .soldier import Dragon
from .soldier import Ninja
from .soldier import Iceman
from .soldier import Lion
from .soldier import Wolf

class HeadQuarter:
    init_element = 0
    soldier_order = {'red':(Iceman, Lion, Wolf, Ninja, Dragon), \
        'blue':(Lion, Dragon, Ninja, Iceman, Wolf)}

    def __init__(self, name):
        self.name = name
        self.enemies = []
        self.__element = self.init_element
        self.soldier_list = []
        self.__soldier_id = 0
        self.__soldier_iter = self.__soldier_generator(self.soldier_order[self.name])

    def __str__(self):
        return self.name + ' headquarter'

    def add_elements(self, number):
        if self.__element + number >= 0:
            self.__element += number
            return True
        return False

    def __soldier_generator(self, order_tuple):
        while True:
            for obj in order_tuple:
                while True:
                    if self.__element >= obj.init_strength:
                        self.__soldier_id += 1
                        yield obj(self, self.__soldier_id, self.__element)
                        break
                    else:
                        yield None

    def make_soldier(self, gametime):
        new_soldier = next(self.__soldier_iter)
        if new_soldier == None:
            return
        self.__element -= new_soldier.init_strength
        self.soldier_list.append(new_soldier)
        
        print(gametime, new_soldier, 'born')
        if new_soldier.remark != None:
            print(new_soldier.remark)
    
    def report_element(self, gametime):
        print(gametime, self.__element, 'elements in', self)