from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert overlapping_intervals((1, 7), (3, 6))
    assert not overlapping_intervals((1, 5), (9, 6))
    assert not overlapping_intervals((6, 5), (3, 6))
    assert overlapping_intervals((1, 5), (1, 6))
    assert overlapping_intervals((2, 5), (4, 6))
    assert overlapping_intervals((1, 6), (3, 9))

    assert not overlapping_intervals((2, 5), (7, 10))