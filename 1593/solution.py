class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max_count = 0
        def backtrack(start, seen):
            if start == len(s):
                self.max_count = max(self.max_count, len(seen))
                return
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if substring not in seen:
                    seen.add(substring)
                    backtrack(i+1, seen)
                    seen.remove(substring)
        backtrack(0, set())
        return self.max_count