class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        for i in range(len(s)-k+1):
            codes.add(s[i:i+k])
            if len(codes) == 2**k:
                return True
        return False