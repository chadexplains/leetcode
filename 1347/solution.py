class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        diff = 0
        for key in s_count.keys():
            diff += abs(s_count[key] - t_count[key])
        return diff