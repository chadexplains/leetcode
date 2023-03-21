class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M == 2:
            if Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
                return 29
            else:
                return 28
        elif M in [4, 6, 9, 11]:
            return 30
        else:
            return 31