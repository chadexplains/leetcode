class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j not in d:
                    d[i+j] = [nums[i][j]]
                else:
                    d[i+j].append(nums[i][j])
        res = []
        for k in sorted(d.keys()):
            res += d[k][::-1]
        return res
