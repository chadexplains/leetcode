class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp_del = [0] * n
        dp_no_del = [0] * n
        dp_del[0] = dp_no_del[0] = arr[0]
        res = arr[0]
        for i in range(1, n):
            dp_no_del[i] = max(dp_no_del[i-1] + arr[i], arr[i])
            dp_del[i] = max(dp_del[i-1] + arr[i], dp_no_del[i-1])
            res = max(res, max(dp_no_del[i], dp_del[i]))
        return res