class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray_code = []
        for i in range(2**n):
            gray_code.append(i ^ i//2)
        start_index = gray_code.index(start)
        return gray_code[start_index:] + gray_code[:start_index]