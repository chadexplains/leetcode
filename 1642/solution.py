def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    diffs = []
    for i in range(len(heights) - 1):
        diff = heights[i+1] - heights[i]
        if diff > 0:
            heapq.heappush(diffs, diff)
            if len(diffs) > ladders:
                bricks -= heapq.heappop(diffs)
                if bricks < 0:
                    return i
    return len(heights) - 1