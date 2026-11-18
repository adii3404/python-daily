class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # 1. Enqueue
    def enqueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    # 2. Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Dequeued Element:", temp.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    # 3. Display
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Queue Contains...")
            temp = self.front
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    # 4. Reverse Queue
    def reverse_queue(self):
        stack = []
        temp = self.front
        while temp:
            stack.append(temp.data)
            temp = temp.next
        self.front = self.rear = None
        while stack:
            self.enqueue(stack.pop())

    # 5. Merge Queue
    def merge_queue(self, q2):
        temp = q2.front
        while temp:
            self.enqueue(temp.data)
            temp = temp.next


# Usage Example
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)

q2 = Queue()
q2.enqueue(30)
q2.enqueue(40)

print("Queue 1 before merge:")
q1.display()

print("Queue 2:")
q2.display()

# Merge q2 into q1
q1.merge_queue(q2)

print("\nQueue 1 after merging q2 into q1:")
q1.display()