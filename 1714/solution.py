def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    heap = []
    for box in boxTypes:
        heapq.heappush(heap, (-box[1], box[0]))
    units = 0
    while truckSize > 0 and heap:
        max_units, boxes = heapq.heappop(heap)
        boxes = min(boxes, truckSize)
        units += boxes * (-max_units)
        truckSize -= boxes
    return units