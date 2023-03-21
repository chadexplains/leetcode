class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for c in s:
            if c == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count