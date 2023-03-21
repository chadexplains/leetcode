class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_ints = set()
        for i in range(20):
            for j in range(20):
                num = x**i + y**j
                if num <= bound:
                    powerful_ints.add(num)
        return list(powerful_ints)