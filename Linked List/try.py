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
            print(current.data,end=" ->")
            current = current.next
        print("None")

    def at_first(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def get_len(self):
        count = 0
        
        current = self.head

        while current:
            count+=1
            current = current.next
        print(f"Total elements in list is {count}")

    def delete(self,target):
        current = self.head
        previous = None

        if current and current.data == target:
            self.head = current.next
            return
        
        while current and current.data != target:
            previous = current
            current = current.next

        if not current:
            print(f"There is no {target} in List")
            return
        
        previous.next = current.next


ll = LinkedList()

while True:
    print("\n--- Linked List Operations ---")
    print("1. Insert at end")
    print("2. Insert at beginning")
    print("3. Display list")
    print("4. Get length")
    print("5. Delete an element")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            data = int(input("Enter data to insert at end: "))
            ll.append(data)
        case "2":
            data = int(input("Enter data to insert at beginning: "))
            ll.at_first(data)
        case "3":
            ll.display()
        case "4":
            ll.get_len()
        case "5":
            target = int(input("Enter value to delete: "))
            ll.delete(target)
        case "6":
            print("Exiting program.")
            break
        case _:
            print("Invalid choice. Please try again.")
