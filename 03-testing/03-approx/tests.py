import pytest
from mystatistics import average

@pytest.mark.parametrize("ns, expected", [
    ([0.1, 0.1, 0.1], 0.1),
    ([1, 2, 3], 2)])
def test_average(ns, expected):
    actual = average(ns)

    assert pytest.approx(actual, abs=0.1) == expected

