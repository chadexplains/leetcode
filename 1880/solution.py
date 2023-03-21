class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        n = len(num)
        nums = [int(x) for x in num]
        for i in range(k):
            j = n - 2
            while j >= 0 and nums[j] >= nums[j+1]:
                j -= 1
            if j < 0:
                break
            l = n - 1
            while l > j and nums[l] <= nums[j]:
                l -= 1
            nums[j], nums[l] = nums[l], nums[j]
            nums[j+1:] = nums[j+1:][::-1]
        sorted_nums = sorted(nums)
        swaps = 0
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                j = i + 1
                while j < n and nums[j] != sorted_nums[i]:
                    j += 1
                nums[i+1:j+1] = nums[i:j]
                nums[i] = sorted_nums[i]
                swaps += j - i
        return swaps