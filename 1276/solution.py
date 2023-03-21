class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0 or tomatoSlices < cheeseSlices * 2 or tomatoSlices > cheeseSlices * 4:
            return []
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo
        return [jumbo, small]