def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    heap = []
    stops = 0
    fuel = startFuel
    pos = 0
    for station in stations + [[target, 0]]:
        while fuel < station[0] - pos:
            if not heap:
                return -1
            fuel += -heapq.heappop(heap)
            stops += 1
        heapq.heappush(heap, -station[1])
        pos = station[0]
    return stops