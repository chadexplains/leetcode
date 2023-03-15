class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = nex
            prev = tail
            head = tail.next
        return dummy.next

    def reverse(self, head, tail):
        prev = tail.next
        curr = head
        while prev != tail:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return tail, head