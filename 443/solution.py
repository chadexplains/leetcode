class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        curr = 0
        for i in range(len(chars)):
            if i == len(chars) - 1 or chars[i] != chars[i+1]:
                chars[write] = chars[curr]
                write += 1
                if i > curr:
                    for digit in str(i - curr + 1):
                        chars[write] = digit
                        write += 1
                curr = i + 1
        return write