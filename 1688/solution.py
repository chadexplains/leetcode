class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1 if n%2==0 else (n-1)//2+1