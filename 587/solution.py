def kClosest(points, k):
    heap = []
    for point in points:
        distance = point[0] ** 2 + point[1] ** 2
        heapq.heappush(heap, (-distance, point))
        if len(heap) > k:
            heapq.heappop(heap)
    return [point for distance, point in heap]