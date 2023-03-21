class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        window = set(S[:K])
        count = 1 if len(window) == K else 0
        for i in range(K, len(S)):
            window.add(S[i])
            window.remove(S[i-K])
            if len(window) == K:
                count += 1
        return count