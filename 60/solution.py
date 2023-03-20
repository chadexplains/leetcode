class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * i)
        k -= 1
        res = []
        for i in range(n-1, -1, -1):
            index = k // factorials[i]
            k %= factorials[i]
            res.append(str(nums[index]))
            nums.pop(index)
        return ''.join(res)