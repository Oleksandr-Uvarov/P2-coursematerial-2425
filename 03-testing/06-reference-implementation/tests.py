import pytest
from student import Student
from search import linear_search, binary_search

@pytest.mark.parametrize("students", [
    [],
    # [[Student(i) for i in range(n)] for n in range(1000)],
    # [Student(i) for i in [1, 3, 4, 5, 9, 11, 26, 77, 103]],
    [Student(i) for i in range(100)]
])
@pytest.mark.parametrize("student_id", 
    range(0, 100),
)
def test_linear_search(students, student_id):
    actual_student = linear_search(students, student_id)

    assert actual_student.id == student_id


@pytest.mark.parametrize("students", [
    [],
    [Student(i) for i in [1, 3, 4, 5, 9, 20, 77, 201, 304]],
    [Student(1) for i in range(100)]
])
@pytest.mark.parametrize("student_id", 
    range(0, 100))
def test_binary_search(students, student_id):
    actual_student = binary_search(students, student_id)

    assert actual_student.id == student_id