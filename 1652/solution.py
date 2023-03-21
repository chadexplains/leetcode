class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted = [0] * n
        for i in range(n):
            s = 0
            for j in range(k):
                s += code[(i+j+1)%n]
            decrypted[i] = s
        return decrypted