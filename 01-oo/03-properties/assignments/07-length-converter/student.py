class LengthConverter:
    def __init__(self):
        self.__distance_in_meters = 0
        self.meter = 0
        self.feet = 0
        self.inch = 0

    @property
    def meter(self):
        return self.__meter
    
    @meter.setter
    def meter(self, value):
        if self.__meter != value:
            self.__meter = value
    
    @property
    def feet(self):
        return self.__feet
    
    @feet.setter
    def feet(self, value):
        if self.__feet != value:
            self.__feet = value

    @property 
    def inch(self):
        return self.__inch

    @inch.setter
    def inch(self, value):
        if self.__inch != value:
            self.__inch = value

