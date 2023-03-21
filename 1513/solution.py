class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        ans = 0
        mod = 10**9 + 7
        for c in s:
            if c == '1':
                count += 1
            else:
                ans += count*(count+1)//2
                count = 0
        ans += count*(count+1)//2
        return ans % mod