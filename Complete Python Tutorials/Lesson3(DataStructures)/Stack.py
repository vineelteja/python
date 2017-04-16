class Stack():
    def __init__(self):
        self.stack = []                                     # start stack with empty list
        self.numOfItems = 0                                 # No items in stack

    def isEmpty(self):                                      # check empty
        return self.stack == []                             # send empty stack

    def push(self, data):                                   # push data into stack
        self.stack.append(data)                             # using inbuit insert push the data
        self.numOfItems += 1                                # add 1 to noOfItems

    def pop(self):                                          # remove element
        self.numOfItems -= 1                                # subtract 1 time
        data = self.stack.pop()                             # pop the data remove it
        return data                                         # return data

    def m_Size(self):
        return len(self.stack)                              # return size

    def print_all(self):
        for each in reversed(self.stack):
            print(each)

stack = Stack()
print("pushing")
stack.push(12)
stack.push(22)
stack.push(23)
print("size ",stack.m_Size())
# print("print all",stack.print_all())
print("popping")
print(stack.pop())
print(stack.pop())
print("size ", end= "")
print(stack.m_Size())
print(stack.print_all())