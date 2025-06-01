from abc import ABC, abstractmethod
import re

class Exercise(ABC):
    def __init__(self, date, distance, duration):
        if not Exercise.is_valid_date(date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        if distance <= 0:
            raise ValueError("Distance must be greater than 0.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
        
        self.date = date
        self.distance = distance
        self.duration = duration

    def __eq__(self, other_activity):
        return self.calories == other_activity.calories
    
    def __lt__(self, other_activity):
        return self.calories < other_activity.calories
    
    def __gt__(self, other_activity):
        return self.calories > other_activity.calories
        
    @staticmethod
    def is_valid_date(date_str):
        # First regex and then the check for individual numbers so that the characters in question are 100% an integer and the conditions don't throw
        # an exception when trying to convert the characters to an integer
        condition = re.fullmatch("[0-9]{4}-[0-9]{2}-[0-9]{2}", date_str)
        if condition == False:
            return False
        
        if int(date_str[5]) not in (0, 1):
            return False
        if int(date_str[8]) > 3:
            return False
        if int(date_str[8]) == 3 and int(date_str[9]) > 1:
            return False

        return True

    @property
    @abstractmethod
    def calories_factor(self):
        ...

    @property   
    @abstractmethod
    def calories(self):
        ...

        

class Run(Exercise):
    def __init__(self, date, distance, duration, elevation):
        super().__init__(date, distance, duration)

        self.elevation = elevation # elevation in percentage

    @property
    def calories_factor(self):
        return 10 * (1 + self.elevation / 100)

    @property
    def calories(self):
        return int((self.distance/(self.duration/60))*self.distance * self.calories_factor)


class Swim(Exercise):
    def __init__(self, date, distance, duration):
        super().__init__(date, distance, duration)
        if distance/duration > 0.1278:
            raise ValueError("You just broke the world record for Swim! Either you are a superhuman or the data is incorrect.")

        self.date = date # date in YYYY-MM-DD format
        self.distance = distance # distance in km
        self.duration = duration # duration in minutes

    @property
    def calories_factor(self):
        return 40

    @property
    def calories(self):
        return int((self.distance/(self.duration/60))*self.distance * self.calories_factor)

class Ride(Exercise):
    def __init__(self, date, distance, duration, elevation):
        super().__init__(date, distance, duration)


        self.elevation = elevation # elevation in percentage

    @property
    def calories_factor(self):
        return 2 * (1 + self.elevation / 100)

    @property
    def calories(self):
        return int((self.distance/(self.duration/60))*self.distance * self.calories_factor)

class ExerciseLog:
    def __init__(self):
        self.__exercises = []

    def add(self, exercise):
        self.__exercises.append(exercise)

    def create_run(self, date, distance, duration, elevation):
        self.add(Run(date, distance, duration, elevation))

    def create_swim(self, date, distance, duration):
        self.add(Swim(date, distance, duration))

    def create_ride(self, date, distance, duration, elevation):
        self.add(Ride(date, distance, duration, elevation))

    def total_calories_burnt(self):
        return sum(exercise.calories for exercise in self.__exercises)
    
    def filter(self, condition):
        lst = []

        for exercise in self.__exercises:
            if condition(exercise):
                lst.append(exercise)

        return lst

    
    def filter_by_date(self, date):
        lst = []

        for exercise in self.__exercises:
            if exercise.date == date:
                lst.append(exercise)

        return lst

    def filter_by_distance(self, min_distance):
        lst = []

        for exercise in self.__exercises:
            if exercise.distance >= min_distance:
                lst.append(exercise)

        return lst


ride = Ride("2001-01-01", 37, 221, "21")

morning_run = Run("2023-10-02", 5, 21, 12)
evening_bike_ride = Ride("2023-10-01", 20, 60, 0)

print(morning_run.calories)
print(evening_bike_ride.calories)

print(morning_run == evening_bike_ride)
print(morning_run < evening_bike_ride)
print(morning_run > evening_bike_ride)

swim = Swim("2001-11-11", 32, 456)