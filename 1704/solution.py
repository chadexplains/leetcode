class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        count = 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                count += 1
            if s[len(s)//2+i] in vowels:
                count -= 1
        return count == 0