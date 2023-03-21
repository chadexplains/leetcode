class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums:
            return []
        res = []
        max_heap = []
        min_heap = []
        for i in range(k):
            heappush(max_heap, -nums[i])
        for i in range(k // 2):
            heappush(min_heap, -heappop(max_heap))
        for i in range(k, len(nums)):
            if k % 2 == 0:
                res.append((-max_heap[0] + min_heap[0]) / 2)
            else:
                res.append(-max_heap[0])
            if nums[i - k] <= -max_heap[0]:
                heappush(max_heap, -nums[i])
                if nums[i - k] <= -max_heap[0]:
                    heappush(min_heap, -heappop(max_heap))
            else:
                heappush(min_heap, nums[i])
                if nums[i - k] <= -max_heap[0]:
                    heappush(min_heap, -heappop(max_heap))
            while max_heap and -max_heap[0] in min_heap:
                heappop(max_heap)
                min_heap.remove(-heappop(max_heap))
        if k % 2 == 0:
            res.append((-max_heap[0] + min_heap[0]) / 2)
        else:
            res.append(-max_heap[0])
        return res