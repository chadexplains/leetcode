class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        cur_len = 1
        max_len = 1
        prev_comp = 0
        for i in range(1, n):
            comp = 0
            if arr[i] > arr[i-1]:
                comp = 1
            elif arr[i] < arr[i-1]:
                comp = -1
            if comp == 0:
                cur_len = 1
            elif comp == prev_comp:
                cur_len = 2
            else:
                cur_len += 1
            max_len = max(max_len, cur_len)
            prev_comp = comp
        return max_len