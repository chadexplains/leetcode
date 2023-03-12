```
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode()
        temp = new_list
        
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        
        return new_list.next
```