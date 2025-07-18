class Queue:
    def __init__(self):
        self.queue = []

    def Enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueued {item}")
    
    def Dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        item = self.queue.pop(0)
        print(f"Dequeued {item}")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        print(self.queue[0])
        return
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        print(len(self.queue))
        return 
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            print(self.queue)
            return

Q1 = Queue()
Q1.Enqueue(10)
Q1.Enqueue(20)
Q1.Enqueue(30)
Q1.Enqueue(40)

Q1.display()

print(Q1.Dequeue())
Q1.peek()
Q1.size()