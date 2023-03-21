class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shift = right_shift = 0
        for direction, amount in shift:
            if direction == 0:
                left_shift += amount
            else:
                right_shift += amount
        net_shift = left_shift - right_shift
        if net_shift < 0:
            net_shift = abs(net_shift)
            direction = 1
        else:
            direction = 0
        net_shift %= len(s)
        if direction == 0:
            return s[net_shift:] + s[:net_shift]
        else:
            return s[-net_shift:] + s[:-net_shift]