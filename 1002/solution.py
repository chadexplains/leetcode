class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        freq = {}
        for char in A[0]:
            freq[char] = freq.get(char, 0) + 1
        for i in range(1, len(A)):
            temp = {}
            for char in A[i]:
                if char in freq:
                    temp[char] = temp.get(char, 0) + 1
            freq = temp
        for char, count in freq.items():
            if count == len(A):
                result.extend([char] * count)
        return result