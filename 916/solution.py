class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        max_freq = [0] * 26
        for word in B:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            for i in range(26):
                max_freq[i] = max(max_freq[i], freq[i])
        res = []
        for word in A:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            if all(freq[i] >= max_freq[i] for i in range(26)):
                res.append(word)
        return res