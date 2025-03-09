# def closest(points, target_point):
#     closest_point = points[0]
#     closest_distance = ((target_point[0] - points[0][0])**2 + (target_point[1] - points[0][1])**2)**0.5

#     x2 = target_point[0]
#     y2 = target_point[1]

#     for point in points:
#         x1 = point[0]
#         y1 = point[1]
        
#         distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#         print(f"x1: {x1}, y1 {y1}, {((x2 - x1)**2 + (y2 - y1)**2)**0.5}")
        
#         if distance < closest_distance:
#             print(f"Changing closest point to {x1}, {y1}")
#             closest_point = point
#             closest_distance = distance
    
#     return closest_point


closest = lambda points, target_point: min(points, key=lambda point: ((target_point[0] - point[0])**2 + (target_point[1] - point[1])**2)**0.5)


points = [(1, 4), (2, 3), (4, 7), (9, 1), (5, 5)]

target_point = (10, 10)

print(closest(points, target_point))