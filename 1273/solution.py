class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0:
            return []
        max_small_burgers = cheeseSlices
        max_tomato_slices = 4 * max_small_burgers + 2 * cheeseSlices
        if tomatoSlices > max_tomato_slices or tomatoSlices < 2 * cheeseSlices:
            return []
        jumbo_burgers = (tomatoSlices - 2 * cheeseSlices) // 2
        small_burgers = cheeseSlices - jumbo_burgers
        return [jumbo_burgers, small_burgers]