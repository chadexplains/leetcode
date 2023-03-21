class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        dp = {-1: 0}
        for i in arr1:
            temp = {}
            for j in dp:
                if i > j:
                    temp[arr2[-1]] = min(temp.get(arr2[-1], float('inf')), dp[j])
                k = bisect.bisect_left(arr2, j)
                if k < len(arr2):
                    temp[arr2[k]] = min(temp.get(arr2[k], float('inf')), dp[j] + 1)
            dp = temp
        if dp:
            return min(dp.values())
        return -1