def removeInterval(intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    result = []
    for interval in intervals:
        if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
            result.append(interval)
        elif interval[0] < toBeRemoved[0] and interval[1] > toBeRemoved[1]:
            result.append([interval[0], toBeRemoved[0]])
            result.append([toBeRemoved[1], interval[1]])
        elif interval[0] < toBeRemoved[0]:
            result.append([interval[0], toBeRemoved[0]])
        elif interval[1] > toBeRemoved[1]:
            result.append([toBeRemoved[1], interval[1]])
    return result