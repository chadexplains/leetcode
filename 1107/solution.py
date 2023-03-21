class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        candies_given = 0
        turn = 0
        while candies_given < candies:
            for i in range(num_people):
                if candies_given < candies:
                    candies_to_give = (turn * num_people) + (i + 1)
                    ans[i] += candies_to_give
                    candies_given += candies_to_give
                else:
                    break
            turn += 1
            candies_given = (turn * num_people * (num_people + 1)) // 2
        ans[-1] += candies - sum(ans)
        return ans