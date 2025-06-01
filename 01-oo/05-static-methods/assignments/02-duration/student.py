class Duration:
    def __init__(self, *, duration_in_seconds):
        self.__seconds = duration_in_seconds

    @property
    def seconds(self):
        return self.__seconds

    @property
    def minutes(self):
        return self.__seconds / 60
    
    @property
    def hours(self):
        return self.__seconds/ 3600
    
    @staticmethod
    def from_hours(number):
        return Duration(duration_in_seconds=number*3600)
    
    @staticmethod
    def from_seconds(number):
        return Duration(duration_in_seconds=number)
    
    @staticmethod
    def from_minutes(number):
        return Duration(duration_in_seconds=number*60)
    

duration = Duration.from_minutes(60)
print(duration.minutes)
print(duration.hours)
print(duration.seconds)