class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        heap = [(-f, w) for w, f in freq.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]