class Solution:
    def findLatestStep(self, nums: List[int], m: int) -> int:
        n = len(nums)
        groups = {n: 1}
        res = -1
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            k = j - i - 1
            if k in groups:
                groups[k] -= 1
                if groups[k] == 0:
                    del groups[k]
            if k == m:
                res = max(res, j - 1 if i == 0 else j - 1 - i)
            if i == 0:
                break
            if j < n and nums[j] != nums[i]:
                if j - i - 1 in groups:
                    groups[j - i - 1] += 1
                else:
                    groups[j - i - 1] = 1
        return res