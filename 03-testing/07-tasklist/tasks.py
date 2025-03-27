class Task:
    def __init__(self, description, due_date):
        self.__description == description
        self.__due_date = due_date
        self.__finished == False

    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def finished(self):
        return self.__finished
    
    @finished.setter
    def finished(self, value):
        self.__finished = value
    
