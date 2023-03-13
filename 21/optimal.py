class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Base case: if either list is empty, return the other list
        if not l1:
            return l2
        if not l2:
            return l1
        
        # Compare the first elements of the two lists and add the smaller one to the result linked list
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
