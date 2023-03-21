def findRightInterval(intervals):
    n = len(intervals)
    start_times = [(interval[0], i) for i, interval in enumerate(intervals)]
    start_times.sort()
    result = [-1] * n
    for i in range(n):
        end_time = intervals[i][1]
        j = bisect_left(start_times, (end_time,))
        if j < n:
            result[i] = start_times[j][1]
    return result