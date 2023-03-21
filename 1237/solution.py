class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        i, j = 1, 1000
        while i <= 1000 and j >= 1:
            val = customfunction.f(i, j)
            if val == z:
                res.append([i, j])
                i += 1
                j -= 1
            elif val < z:
                i += 1
            else:
                j -= 1
        return res