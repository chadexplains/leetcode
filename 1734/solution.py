class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        xor_all = reduce(xor, range(1, n+1))
        xor_encoded = reduce(xor, encoded)
        first = xor_all ^ xor_encoded
        perm = [first]
        for i in range(n-2):
            perm.append(perm[-1] ^ encoded[i])
        return perm