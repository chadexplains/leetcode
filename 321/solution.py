class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max(nums, k):
            stack = []
            n = len(nums)
            for i in range(n):
                while stack and len(stack) + n - i > k and stack[-1] < nums[i]:
                    stack.pop()
                if len(stack) < k:
                    stack.append(nums[i])
            return stack
        
        def merge(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    res.append(nums2[0])
                    nums2 = nums2[1:]
            return res
        
        m, n = len(nums1), len(nums2)
        res = [0] * k
        for i in range(max(0, k - n), min(k, m) + 1):
            max1 = get_max(nums1, i)
            max2 = get_max(nums2, k - i)
            cur = merge(max1, max2)
            if cur > res:
                res = cur
        return res