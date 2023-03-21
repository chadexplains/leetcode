class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        n = len(s)
        start = 0
        for i in range(rows):
            start += cols
            if s[start % n] == ' ':
                start += 1
            elif s[(start-1) % n] != ' ':
                while start > 0 and s[(start-1) % n] != ' ':
                    start -= 1
            else:
                while s[start % n] != ' ':
                    start += 1
        return start // n