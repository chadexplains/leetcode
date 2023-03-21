class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        heap = []
        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))
        result = []
        while heap:
            count, char = heapq.heappop(heap)
            result.extend([char] * -count)
        return ''.join(result)