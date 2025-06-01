from student import Swim
import pytest

def test_valid_constructor():
    Swim("2001-01-01", 21, 221)

@pytest.mark.parametrize("date", [
    "2001-32-11",
    "23142412412",
    "10000-02-11",
    "2001-11-32",
])
def test_raises_error_when_invalid_date_and_duration(date):
    with pytest.raises(ValueError):
        Swim(date, 12, 221)

def test_raises_error_when_invalid_distance_and_duration():
    with pytest.raises(ValueError):
        Swim("2001-01-01", 37, 221)

def test_raises_error_when_negative_distance():
    with pytest.raises(ValueError):
        Swim("2001-01-01", -37, 221)

def test_raises_error_when_negative_duration():
    with pytest.raises(ValueError):
        Swim("2001-01-01", 21, -221)

@pytest.mark.parametrize("distance, duration, expected_calories", [
    [12, 201, 1719],
    [21, 234, 4523],
    [33, 321, 8142],
    [40, 480, 8000]
])
def test_expected_calories(distance, duration, expected_calories):
    assert Swim("2001-01-01", distance, duration).calories == expected_calories
