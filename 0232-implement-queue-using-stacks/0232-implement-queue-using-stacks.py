class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1 and not self.stack2:
            return
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        
    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            return self.stack1[0]
        else:
            return

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()