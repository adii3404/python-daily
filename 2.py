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
        else:
            temp = self.top
            print('Poped Element :- ', temp.data)
            self.top = self.top.next
            temp = None

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


# Usage Example
s = Stack()
print(s.reverse_string('sumit'))