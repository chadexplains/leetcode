```python
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start, end, count = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] >= left and nums[i] <= right:
                end = i
                count += end - start + 1
            elif nums[i] < left:
                count += end - start + 1
            else:
                start = i + 1
                end = i
        return count
```