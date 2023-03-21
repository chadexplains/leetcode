class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        unique_or = set()
        cur_or = set()
        for num in A:
            cur_or = {num | prev for prev in cur_or} | {num}
            unique_or |= cur_or
        return len(unique_or)