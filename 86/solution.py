class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = less_head = ListNode(0)
        greater = greater_head = ListNode(0)
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        greater.next = None
        less.next = greater_head.next
        return less_head.next