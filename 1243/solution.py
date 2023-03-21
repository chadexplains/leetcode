class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        prev = arr.copy()
        changed = True
        while changed:
            changed = False
            for i in range(1, len(arr) - 1):
                if prev[i] < prev[i - 1] and prev[i] < prev[i + 1]:
                    arr[i] += 1
                    changed = True
                elif prev[i] > prev[i - 1] and prev[i] > prev[i + 1]:
                    arr[i] -= 1
                    changed = True
            prev = arr.copy()
        return arr