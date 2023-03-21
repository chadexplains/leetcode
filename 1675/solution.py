class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            max_divisor = num
            while num % 2 == 0:
                num //= 2
                max_divisor *= 2
            heap.append((num, max_divisor))
        min_num = min(num for num, _ in heap)
        max_deviation = max(max_divisor for _, max_divisor in heap)
        min_deviation = max_deviation - min_num
        heapq.heapify(heap)
        while heap:
            num, max_divisor = heapq.heappop(heap)
            if num % 2 == 1:
                break
            num //= 2
            max_divisor //= 2
            heapq.heappush(heap, (num, max_divisor))
            min_num = min(min_num, num)
            min_deviation = min(min_deviation, max_deviation - min_num)
        return min_deviation