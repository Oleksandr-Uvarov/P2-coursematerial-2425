class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter 
    def hours(self, value):
        if 0 <= value <= 23:
            self.__hours = value
        else:
            raise ValueError("Can't be less than 0 or more than 23")
    
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter 
    def minutes(self, value):
        if 0 <= value <= 59:
            self.__minutes = value
        else:
            raise ValueError("Can't be less than 0 or more than 59")
        
    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter 
    def seconds(self, value):
        if 0 <= value <= 59:
            self.__seconds = value
        else:
            raise ValueError("Can't be less than 0 or more than 59")
        

# time = Time(0, 0, 0)
# time.hours = 8
# time.minutes = -1