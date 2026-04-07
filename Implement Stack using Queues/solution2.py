class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Queue:
    def __init__(self):
        self.front_node = None
        self.back_node = None
        self.count = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.back_node is None:
            self.front_node = new_node
            self.back_node = new_node
        else:
            self.back_node.next = new_node
            self.back_node = new_node
        self.count += 1

    def pop(self) -> int:
        value = self.front_node.value
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.back_node = None
        self.count -= 1
        return value

    def peek(self) -> int:
        return self.front_node.value

    def empty(self) -> bool:
        return self.front_node is None

    def size(self) -> int:
        return self.count


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.push(x)
        while not self.q1.empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
