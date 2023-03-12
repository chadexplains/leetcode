class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        current = result
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        return result.next
