class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def isEmpty(self):
        return self.top is None

    def push(self, new_node):
        temp = Node(new_node)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return None
        else:
            temp = self.top
            self.top = self.top.next
            data = temp.data
            temp = None
            return data

    def print(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            print('Stack Contains...')
            temp = self.top
            while temp:
                print(temp.data, end=' -> ')
                temp = temp.next
            print('Null')

    def reverse_string(self, data):
        stack = []
        for ch in data:
            stack.append(ch)
        result = ""
        while stack:
            result += stack.pop()
        return result

    def reverse_stack(self, s1, s2):
        while not s1.isEmpty():
            s2.push(s1.pop())


# ==========================================
# Usage Examples
# ==========================================

# 1. Basic Stack Operations
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print()

print('\nAfter a Pop Operation :- ')
s.pop()
s.print()

# 2. Reverse String using Stack
print('\n--- Reverse String ---')
print(s.reverse_string('sumit'))

# 3. Reverse Stack using Another Stack
print('\n--- Reverse Stack using Another Stack ---')
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)

print('Original Stack 1:')
s1.print()

s2 = Stack()
s.reverse_stack(s1, s2)

print('Reversed Stack (Stack 2):')
s2.print()