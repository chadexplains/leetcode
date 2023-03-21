class Solution:
    def findFollowersCount(self, matrix: List[List[int]]) -> List[int]:
        follower_count = {}
        for row in matrix:
            for i, val in enumerate(row):
                if val == 1:
                    if i in follower_count:
                        follower_count[i] += 1
                    else:
                        follower_count[i] = 1
        return list(follower_count.values())