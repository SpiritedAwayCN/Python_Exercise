class Timer:
    def __init__(self):
        self.hour, self.minute = 0, 0
    
    def __str__(self):
        return "%03d"%self.hour

    def next_hour(self):
        self.hour += 1
        self.minute = 0