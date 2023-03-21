class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = {}
        result = []
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            bitmask = 0
            for char in substring:
                bitmask <<= 2
                if char == 'A':
                    bitmask |= 0b00
                elif char == 'C':
                    bitmask |= 0b01
                elif char == 'G':
                    bitmask |= 0b10
                elif char == 'T':
                    bitmask |= 0b11
            freq[bitmask] = freq.get(bitmask, 0) + 1
            if freq[bitmask] == 2:
                result.append(substring)
        return result