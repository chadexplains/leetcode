class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0
        while head:
            decimal_value = (decimal_value << 1) | head.val
            head = head.next
        return decimal_value