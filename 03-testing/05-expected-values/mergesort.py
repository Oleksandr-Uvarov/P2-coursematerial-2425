def split_in_two(ns):
    len_ns_1 = len(ns) // 2
    return (ns[0:len_ns_1], ns[len_ns_1:])


def merge_sorted(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i == len(left):
        result += right[j:]
    else:
        result += left[i:]

    return result



print(merge_sorted([1, 2, 1, 3, 2], [1, 1, 2, 3, 4, 5, 6, 6, 7, 7, 2, 10, 11]))
