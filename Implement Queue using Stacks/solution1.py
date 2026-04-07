class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self) -> int:
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self) -> int:
        return self.top.value

    def empty(self) -> bool:
        return self.top is None


class MyQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def pop(self) -> int:
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.empty() and self.stack_out.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
