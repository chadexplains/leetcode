class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        for i in range(len(num)-1, -1, -1):
            carry, num[i] = divmod(num[i] + carry, 10)
        if carry:
            num.insert(0, carry)
        return num