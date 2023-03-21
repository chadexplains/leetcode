class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        can_break = None
        for i in range(len(s1)):
            if s1[i] >= s2[i]:
                continue
            elif s2[i] >= s1[i]:
                can_break = False
                break
        if can_break is None:
            can_break = True
        return can_break