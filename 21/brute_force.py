class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        curr = new_head
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return new_head.next
