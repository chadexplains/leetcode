class MaxStack:
    
    def __init__(self):
        self.stack = []
        self.max_stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        
    def pop(self) -> int:
        x = self.stack.pop()
        if x == self.max_stack[-1]:
            self.max_stack.pop()
        return x
        
    def top(self) -> int:
        return self.stack[-1]
        
    def peekMax(self) -> int:
        return self.max_stack[-1]
        
    def popMax(self) -> int:
        max_val = self.max_stack.pop()
        temp = []
        while self.stack[-1] != max_val:
            temp.append(self.stack.pop())
        self.stack.pop()
        while temp:
            self.push(temp.pop())
        return max_val