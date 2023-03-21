class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        n = len(S)
        if n == 0:
            return ''
        first_group_len = n % K
        if first_group_len == 0:
            first_group_len = K
        res = S[:first_group_len]
        for i in range(first_group_len, n, K):
            res += '-' + S[i:i+K]
        return res[::-1]