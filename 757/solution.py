def intersectionSizeTwo(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    last, second_last = -1, -1
    for start, end in intervals:
        if start > last:
            count += 2
            second_last, last = last, end
        elif start > second_last:
            count += 1
            second_last, last = last, end
    return count