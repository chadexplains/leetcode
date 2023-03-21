class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        deletions = 0
        for c in s:
            if c == 'a':
                count += 1
            elif count > 0:
                count -= 1
                deletions += 1
        return deletions