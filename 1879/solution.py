class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(num):
            i = len(num) - 2
            while i >= 0 and num[i] >= num[i+1]:
                i -= 1
            if i < 0:
                return num
            j = len(num) - 1
            while j >= 0 and num[j] <= num[i]:
                j -= 1
            num[i], num[j] = num[j], num[i]
            num[i+1:] = reversed(num[i+1:])
            return num
        nums = list(num)
        for _ in range(k):
            nums = next_permutation(nums)
        sorted_nums = sorted(list(map(''.join, permutations(nums))))
        ans = 0
        for i in range(len(num)):
            if num[i] != sorted_nums[i]:
                j = i + 1
                while j < len(num) and sorted_nums[j] != num[i]:
                    j += 1
                ans += j - i
                sorted_nums[i+1:j+1] = sorted(sorted_nums[i:j+1])
        return ans