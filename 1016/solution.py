class Solution:
    def queryString(self, S: str, N: int) -> bool:
        min_len = len(bin(N)[2:])
        for i in range(1, N+1):
            binary = bin(i)[2:]
            if len(binary) < min_len:
                binary = '0'*(min_len-len(binary)) + binary
            if binary not in S:
                return False
        return True