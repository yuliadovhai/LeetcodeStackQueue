from collections import defaultdict, deque


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.groups[f].append(val)
        if f > self.max_freq:
            self.max_freq = f

    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
