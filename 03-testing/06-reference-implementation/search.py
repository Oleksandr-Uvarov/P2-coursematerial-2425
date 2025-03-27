from student import Student
from math import ceil, floor

def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None


def binary_search(students, target_id):
    left = 0
    right = len(students)

    while left < right:
        middle_index = (left + right) // 2

        middle = students[middle_index]
        middle_id = middle.id

        if middle_id == target_id:
            return middle

        if middle_id < target_id:
            right = middle_index - 1
        
        if middle_id > target_id:
            left = middle_index + 1

    return None

student_0 = Student(0)
student_1 = Student(1)
student_2 = Student(2)
student_3 = Student(3)
student_4 = Student(4)
student_5 = Student(5)
student_6 = Student(6)
student_7 = Student(7)
student_8 = Student(8)
student_9 = Student(9)
student_10 = Student(10)
student_11 = Student(11)
student_12 = Student(12)
student_13 = Student(13)
student_14 = Student(14)
student_15 = Student(15)
student_16 = Student(16)

students = [student_0, student_1, student_2, student_3, student_4, student_5, student_6, student_7,
            student_8, student_9, student_10, student_11, student_12, student_13, student_14,
            student_15, student_16]

students_2 = [Student(i) for i in range(100)]

print(binary_search(students, 10))
print(binary_search(students, 0))
print(binary_search(students, 11))
print(binary_search(students, 16))

print(binary_search(students_2, 99))













def binary_search(students, target_id):

    if len(students) == 0:
        return None
    
    if target_id > students[-1].id:
        return None
    
    if target_id < students[0].id:
        return None

    left_index = 0
    right_index = len(students) - 1

    left = students[left_index]
    right = students[right_index]

    middle_index = left_index + right_index // 2
    middle = students[middle_index]

    i = 0
    while left_index < right_index: 
    # while middle.id != target_id:        
        if middle.id > target_id:
            right_index = middle_index
            # middle_index = floor((left_index + right_index) / 2)
        if middle.id < target_id:
            left_index = middle_index + 1
            # middle_index = ceil((left_index + right_index) / 2)

        middle_index = (left_index + right_index) // 2

        middle = students[middle_index]
        if middle.id == target_id:
            return middle
        
        i += 1
        # if i > 100:
        #     # return f"Target id: {target_id}, Found id: {middle.id}"
        #     return None

        # if middle.id == target_id:
        #     return middle
    # print(f"Target id: {target_id}, Found id: {middle.id}")
    return None