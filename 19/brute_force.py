class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length == n:
            return head.next
        node = head
        for i in range(length - n - 1):
            node = node.next
        node.next = node.next.next
        return head
