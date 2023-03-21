class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        rank_dict = {}
        rank = 1
        for num in sorted_arr:
            if num not in rank_dict:
                rank_dict[num] = rank
                rank += 1
        return [rank_dict[num] for num in arr]