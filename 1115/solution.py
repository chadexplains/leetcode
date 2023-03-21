class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.foo_done = threading.Condition(self.lock)
        self.bar_done = threading.Condition(self.lock)
        self.counter = 0

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.lock:
                while self.counter % 2 == 1:
                    self.foo_done.wait()
                printFoo()
                self.counter += 1
                self.bar_done.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.lock:
                while self.counter % 2 == 0:
                    self.bar_done.wait()
                printBar()
                self.counter += 1
                self.foo_done.notify()

fooBar = FooBar(n)
thread1 = threading.Thread(target=fooBar.foo, args=(printFoo,))
thread2 = threading.Thread(target=fooBar.bar, args=(printBar,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()