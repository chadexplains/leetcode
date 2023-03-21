class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        transpose = []
        for i in range(len(words[0])):
            transpose.append(''.join([word[i] if i < len(word) else '' for word in words]))
        return words == transpose