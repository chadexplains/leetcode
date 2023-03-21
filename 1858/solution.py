class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in s:
            i = t.find(c, i)
            if i == -1:
                return False
            i += 1
        return True

    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            if self.isSubsequence(word, s):
                return word
        return ""