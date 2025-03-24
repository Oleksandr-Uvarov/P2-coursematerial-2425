def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2


    one = left1 <= right1 and left1 <= right2
    two = left2 <= right2 and left2 <= right1

    return one and two