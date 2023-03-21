class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res = float('inf')
        s = set()
        for a in arr:
            new_s = set()
            for x in s:
                new_s.add(x&a)
            new_s.add(a)
            s = new_s
            for x in s:
                res = min(res, abs(x - target))
        return res