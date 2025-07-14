class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def insert_at_first(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def get_length(self):
        counter = 0

        iteration = self.head

        while iteration:
            counter+=1
            iteration= iteration.next
        print(f"There are total {counter} Elements in Linked List")

LL = LinkedList()
LL.append(10)
LL.append(20)
LL.append(30)
        
LL.display()

LL.insert_at_first(32)

LL.display()

LL.get_length()