import pytest
from mergesort import split_in_two, merge_sorted

@pytest.mark.parametrize("ns", [
    [k for k in range(n)] for n in range(1000)
])
def test_split_in_two(ns):
    ns_1, ns_2 = split_in_two(ns)
    assert ns == ns_1 + ns_2

@pytest.mark.parametrize('left', [
    [],
    [1],
    [4, 10, 15],
    [1, 2, 3, 4, 5, 6, 6, 7, 7, 10, 11],
    [-1, 2, 3, 41, 1234]

    # ...
])
@pytest.mark.parametrize('right', [
    [],
    [1],
    [2, 5, 5, 9],
    [2, 2, 2, 2, 4, 4],
    [1, 2, 2, 2]
    # ...
])
def test_merge_sorted(left, right):
    assert sorted(left + right) == merge_sorted(left, right)