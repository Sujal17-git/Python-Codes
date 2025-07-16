class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        print(f"Pushed {data}")

    def display(self):
        current = self.head
        print("Stack Top -> Bottom",end =" ")
        while current:
            print(current.data,end=" ")
            current=current.next
        print()

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        else:
            popped = self.head.data
            self.head = self.head.next   # ✅ FIXED
            return popped

    
    def is_empty(self):
        return self.head is None
    

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
print(s.pop())
print(s.pop())
print(s.pop())