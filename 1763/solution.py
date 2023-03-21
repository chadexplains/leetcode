class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, curr):
            if len(set(curr)) != len(curr):
                return
            nonlocal ans
            ans = max(ans, len(curr))
            if index == len(arr):
                return
            for i in range(index, len(arr)):
                backtrack(i + 1, curr + arr[i])
        ans = 0
        backtrack(0, "")
        return ans