def rearrangeString(s: str, k: int) -> str:
    if k == 0:
        return s
    freq = collections.Counter(s)
    heap = [(-f, c) for c, f in freq.items()]
    heapq.heapify(heap)
    res = []
    while heap:
        temp = []
        for _ in range(min(k, len(s)))):
            if not heap:
                return ""
            f, c = heapq.heappop(heap)
            res.append(c)
            if f + 1:
                temp.append((f + 1, c))
        for item in temp:
            heapq.heappush(heap, item)
        
    return ''.join(res)