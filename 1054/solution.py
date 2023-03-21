class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = collections.Counter(barcodes)
        heap = [(-f, b) for b, f in freq.items()]
        heapq.heapify(heap)
        result = [0] * len(barcodes)
        i = 0
        while heap:
            f, b = heapq.heappop(heap)
            for _ in range(-f):
                if i >= len(result):
                    i = 1
                result[i] = b
                i += 2
        return result