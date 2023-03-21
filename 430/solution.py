def flatten(self, head: 'Node') -> 'Node':
    if not head:
        return None
    stack = []
    current = head
    while current:
        if current.child:
            if current.next:
                stack.append(current.next)
            current.next = current.child
            current.next.prev = current
            current.child = None
        elif not current.next and stack:
            current.next = stack.pop()
            current.next.prev = current
        current = current.next
    return head