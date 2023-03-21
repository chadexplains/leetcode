class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        median = self.findKthLargest(nums, (n + 1) // 2)
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[self.newIndex(i, n)] > median:
                nums[self.newIndex(left, n)], nums[self.newIndex(i, n)] = nums[self.newIndex(i, n)], nums[self.newIndex(left, n)]
                left += 1
                i += 1
            elif nums[self.newIndex(i, n)] < median:
                nums[self.newIndex(right, n)], nums[self.newIndex(i, n)] = nums[self.newIndex(i, n)], nums[self.newIndex(right, n)]
                right -= 1
            else:
                i += 1
        
        for i in range(1, (n + 1) // 2, 2):
            nums[self.newIndex(i, n)], nums[self.newIndex(n // 2 + i, n)] = nums[self.newIndex(n // 2 + i, n)], nums[self.newIndex(i, n)]
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
    
    def newIndex(self, index, n):
        return (1 + 2 * index) % (n | 1)