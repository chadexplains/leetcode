class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        res = str(num1 + num2)
        dummy = ListNode(-1)
        cur = dummy
        for char in res:
            cur.next = ListNode(int(char))
            cur = cur.next
        return dummy.next
