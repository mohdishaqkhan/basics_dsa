"""Implement a stack that can return its minimum in O(1) time."""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def get_min(self):
        if not self.min_stack:
            raise IndexError("minimum of empty stack")
        return self.min_stack[-1]

if __name__ == "__main__":
    s = MinStack()
    for value in map(int, input("Enter stack values separated by spaces: ").split()):
        s.push(value)
    if s.stack:
        print("Stack:", s.stack)
        print("Minimum:", s.get_min())
    else:
        print("Stack is empty")
