def longestDiverseString(a: int, b: int, c: int) -> str:
    freq = {'a': a, 'b': b, 'c': c}
    heap = [(-value, key) for key, value in freq.items()]
    heapq.heapify(heap)
    result = []
    while heap:
        freq, char = heapq.heappop(heap)
        if len(result) >= 2 and result[-1] == result[-2] == char:
            if not heap:
                break
            freq2, char2 = heapq.heappop(heap)
            result.append(char2)
            heapq.heappush(heap, (freq, char))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, char2))
        else:
            result.append(char)
            if freq + 1 < 0:
                heapq.heappush(heap, (freq + 1, char))
    return ''.join(result)