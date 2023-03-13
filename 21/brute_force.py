class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a new linked list
        dummy = ListNode(0)
        curr = dummy
        
        # Traverse through both linked lists
        while l1 and l2:
            # Compare the first elements of the two lists
            if l1.val < l2.val:
                # Add the smaller element to the new linked list
                curr.next = l1
                l1 = l1.next
            else:
                # Add the smaller element to the new linked list
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # Add the remaining elements of the non-empty list to the new linked list
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        # Return the head of the new linked list
        return dummy.next
