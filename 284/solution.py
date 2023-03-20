class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.cache = None

    def peek(self):
        if self.cache is None:
            self.cache = self.iterator.next()
        return self.cache

    def next(self):
        if self.cache is not None:
            result = self.cache
            self.cache = None
            return result
        else:
            return self.iterator.next()

    def hasNext(self):
        return self.cache is not None or self.iterator.hasNext()