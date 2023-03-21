class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return None
        head = self.reverseList(head)
        carry = 1
        curr = head
        while curr:
            carry, curr.val = divmod(curr.val + carry, 10)
            if carry and not curr.next:
                curr.next = ListNode(0)
            curr = curr.next
        return self.reverseList(head)
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev