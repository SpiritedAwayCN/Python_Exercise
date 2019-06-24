from .timer import Timer
from .headquarter import HeadQuarter
from .soldier import Soldier

def Run():
    redHQ = HeadQuarter('red')
    blueHQ = HeadQuarter('blue')
    gametime = Timer()

    while True:
        gametime.minute = 0
        redHQ.make_soldier(gametime)
        blueHQ.make_soldier(gametime)
        if redHQ.lose and blueHQ.lose:
            break
        
        gametime.next_hour()