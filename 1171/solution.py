def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    hash_table = {0: dummy}
    while head:
        prefix_sum += head.val
        if prefix_sum in hash_table:
            node_to_remove = hash_table[prefix_sum].next
            temp_sum = prefix_sum
            while node_to_remove != head:
                temp_sum += node_to_remove.val
                del hash_table[temp_sum]
                node_to_remove = node_to_remove.next
            hash_table[prefix_sum].next = head.next
        else:
            hash_table[prefix_sum] = head
        head = head.next
    return dummy.next