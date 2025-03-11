class LengthConverter:
    def __init__(self):
        self.__distance_in_meters = 0
        self.feet = 0
        self.inch = 0

    @property
    def meter(self):
        return self.__distance_in_meters
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_meters = value
    
    @property
    def feet(self):
        return self.__distance_in_meters * 3.28084
    
    @feet.setter
    def feet(self, value):
        self.__distance_in_meters = value / 3.28084

    @property 
    def inch(self):
        return self.__distance_in_meters * 39.3701

    @inch.setter
    def inch(self, value):
        self.__distance_in_meters = value / 39.3701

converter = LengthConverter()
converter.meter = 100