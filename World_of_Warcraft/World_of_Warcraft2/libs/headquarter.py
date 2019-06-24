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
        self.lose = False
        self.__element = self.init_element
        self.__soldier_list = []
        self.__soldier_count = {'dragon':0, 'ninja':0, 'iceman':0, 'lion':0, 'wolf':0}
        self.__soldier_id = 0
        self.__soldier_iter = self.__soldier_generator(self.soldier_order[self.name])

    def __str__(self):
        return self.name + ' headquarter'

    def __soldier_generator(self, order_tuple):
        cnt = 0
        while True:
            for obj in order_tuple:
                if self.__element >= obj.init_strength:
                    cnt = 0
                    self.__soldier_id += 1
                    yield obj(self, self.__soldier_id, self.__element)
            cnt += 1
            if cnt >=2:
                break

    def make_soldier(self, gametime):
        if self.lose:
            return
        try:
            new_soldier = next(self.__soldier_iter)
        except StopIteration:
            print(gametime, self, "stops making warriors")
            self.lose = True
            return
        self.__element -= new_soldier.init_strength
        self.__soldier_list.append(new_soldier)
        self.__soldier_count[new_soldier.type_name()] += 1

        print(gametime, new_soldier, 'born with strength %d,%d'% \
            (new_soldier.strength, self.__soldier_count[new_soldier.type_name()]), \
            new_soldier.type_name(), 'in', self)
        if new_soldier.remark != None:
            print(new_soldier.remark)