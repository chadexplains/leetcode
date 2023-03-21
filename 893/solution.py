class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = set()
        for s in A:
            even = sorted(s[::2])
            odd = sorted(s[1::2])
            groups.add(''.join(even + odd))
        return len(groups)