class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        index_map = {}
        for i, num in enumerate(B):
            index_map[num] = i
        result = []
        for num in A:
            result.append(index_map[num])
        return result