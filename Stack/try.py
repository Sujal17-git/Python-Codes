class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, item):
        self.stack.append(item)

    # Pop operation
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    # Peek (top element)
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack from top to bottom:", self.stack[::-1])
