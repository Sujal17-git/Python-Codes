class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")

    def delete(self,target):
        current = self.head
        previous = None

        if current and current.data ==target:
            self.head = current.next
            return

        while current and current.data != target:
            previous = current
            current = current.next

        if not current:
            print(f"There is no {target} in this list")
            return
        previous.next = current.next

    def get_len(self):
        count = 0
        current = self.head

        while current:
            count+=1
            current = current.next
        print(f"there are {count} elements in linked list")

    def append_at_first(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.display()
ll.delete(30)
ll.display()
ll.get_len()
ll.append_at_first(5)
ll.display()