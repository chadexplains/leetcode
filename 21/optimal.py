class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            merged_list = l1
            merged_list.next = self.mergeTwoLists(l1.next, l2)
        else:
            merged_list = l2
            merged_list.next = self.mergeTwoLists(l1, l2.next)
        
        return merged_list
