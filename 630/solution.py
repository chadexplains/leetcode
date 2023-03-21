def scheduleCourse(self, courses: List[List[int]]) -> int:
    courses.sort(key=lambda x: x[1])
    pq = []
    time = 0
    for duration, end in courses:
        if time + duration <= end:
            heapq.heappush(pq, -duration)
            time += duration
        elif pq and -pq[0] > duration:
            time += heapq.heappop(pq) + duration
            heapq.heappush(pq, -duration)
    return len(pq)