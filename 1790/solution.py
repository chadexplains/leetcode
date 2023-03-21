class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        target.sort()
        arr.sort()
        return target == arr