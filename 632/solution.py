```python
import heapq
def smallestRange(nums):
    heap = [(row[0], i, 0) for i, row in enumerate(nums)]
    heapq.heapify(heap)
    ans = [-1e9, 1e9]
    right = max(row[0] for row in nums)
    while heap:
        left, i, j = heapq.heappop(heap)
        if right - left < ans[1] - ans[0]:
            ans = [left, right]
        if j + 1 == len(nums[i]):
            return ans
        v = nums[i][j+1]
        right = max(right, v)
        heapq.heappush(heap, (v, i, j+1))
    return ans
```