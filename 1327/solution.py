def removeInterval(intervals, toBeRemoved):
    remaining = []
    for interval in intervals:
        if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
            remaining.append(interval)
        elif interval[0] < toBeRemoved[0] and interval[1] > toBeRemoved[1]:
            remaining.append([interval[0], toBeRemoved[0]])
            remaining.append([toBeRemoved[1], interval[1]])
        elif interval[0] < toBeRemoved[0]:
            remaining.append([interval[0], toBeRemoved[0]])
        elif interval[1] > toBeRemoved[1]:
            remaining.append([toBeRemoved[1], interval[1]])
    return remaining