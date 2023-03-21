def smallestChair(seats: List[List[int]], arrivals: List[int], target: int) -> int:
    occupied = set()
    unoccupied = []
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] not in occupied:
                unoccupied.append(seats[i][j])
    unoccupied.sort()
    arrivals = [(arrivals[i], i) for i in range(len(arrivals))]
    arrivals.sort()
    for arrival, i in arrivals:
        if not unoccupied:
            return -1
        chair = heapq.heappop(unoccupied)
        while unoccupied and unoccupied[0] == chair:
            heapq.heappop(unoccupied)
        occupied.add(chair)
        if i == target - 1:
            return unoccupied.index(chair)