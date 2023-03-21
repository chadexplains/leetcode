class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        result = 0
        table = {0: -1}
        for i, c in enumerate(s):
            mask ^= 1 << int(c)
            if mask in table:
                result = max(result, i - table[mask])
            for j in range(10):
                alt_mask = mask ^ (1 << j)
                if alt_mask in table:
                    result = max(result, i - table[alt_mask])
            if mask not in table:
                table[mask] = i
        return result