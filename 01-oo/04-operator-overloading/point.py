class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __add__(self, point):
        return Point(self.x + point.x,
                     self.y + point.y)



point1 = Point(3, 4)
point2 = Point(2, 5)

point3 = point1 + point2

print(point3.x, point3.y)