def insert(self, head: 'Node', insertVal: int) -> 'Node':
    new_node = Node(insertVal)
    if not head:
        new_node.next = new_node
        return new_node
    prev, curr = head, head.next
    while curr != head:
        if prev.val <= insertVal <= curr.val:
            break
        if prev.val > curr.val and (insertVal < curr.val or insertVal > prev.val):
            break
        prev, curr = curr, curr.next
    prev.next = new_node
    new_node.next = curr
    return head