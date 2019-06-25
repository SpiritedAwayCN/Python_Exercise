class Timer:
    def __init__(self):
        self.hour, self.minute = 0, 0
    
    def __str__(self):
        return "%03d:%02d"%(self.hour, self.minute)

    def next_hour(self):
        self.hour += 1
        self.minute = 0
    
    def total_minute(self):
        return self.hour * 60 + self.minute