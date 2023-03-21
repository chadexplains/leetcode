class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, mask):
            if index == len(arr):
                return bin(mask).count('1')
            m1 = mask
            for c in arr[index]:
                m2 = 1 << (ord(c) - ord('a'))
                if m1 & m2:
                    continue
                if backtrack(index + 1, m1 | m2) == -1:
                    return -1
                m1 |= m2
            return bin(m1).count('1')
        return backtrack(0, 0)