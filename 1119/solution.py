class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        result = ''
        for c in S:
            if c not in vowels:
                result += c
        return result