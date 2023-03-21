class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        a = s.replace(max(s), '9')
        b = s.replace(min(filter(lambda x: x != '0', s)), '1')
        return int(a) - int(b)