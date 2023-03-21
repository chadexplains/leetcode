class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            i = 0
            for c in t:
                if i < len(s) and s[i] == c:
                    i += 1
            return i == len(s)
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, strs[j]) for j in range(i)):
                return len(s)
        return -1