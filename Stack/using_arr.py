class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
        return f"{data} Pushed"
    
    def display(self):
        if self.is_empty():
            print ("stack underflow!")
        else:
            print(f"Stack Top->Bottom {self.stack[::-1]}")

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        self.stack.pop()
        return self.stack[::-1]

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.push(50)
s.display()
print(s.peek())
print(s.pop())




