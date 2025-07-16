class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
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
        new_node.previous = last

    def display(self):
        current = self.head

        while current:
            print(current.data,end =" <-> ")
            current = current.next
        print("None")

    def add_at_first(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        
    def get_len(self):
        current = self.head
        count = 0

        while current:
            count+=1
            current=current.next
        print(f"total Elements in list are {count}")

    def delete(self, value):
        current = self.head

        while current:
            if current.data == value:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next  # Deleting the head

                if current.next:
                    current.next.previous = current.previous
                return
            current = current.next

        print(f"{value} not found.")





ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.display()    
ll.get_len()
ll.delete(20)
ll.display()