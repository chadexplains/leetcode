def deckRevealedIncreasing(deck):
    deck.sort(reverse=True)
    queue = collections.deque()
    for card in deck:
        queue.appendleft(card)
        if len(queue) > 1:
            queue.appendleft(queue.pop())
    return reversed(queue)