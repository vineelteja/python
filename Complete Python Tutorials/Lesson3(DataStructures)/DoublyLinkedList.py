class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.next is None and current_node.prev is None:   # Remove when there is only single element
                    self.head = current_node.next
                    self.size -= 1
                elif current_node.next is None:                               # Remove the last element
                    current_node.prev.next = None
                    self.size -= 1
                elif current_node.prev is not None:                           # Remove the element anywhere in middle
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    self.size -= 1
                else:                                                         # Remove the head element
                    self.head = current_node.next
                    current_node.next.prev = None
                    self.size -= 1
            current_node = current_node.next
        print("Value Not found", data)


    def list_size(self):
        return self.size

    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next




link = DoubleList()
link.insert(10)
link.insert(20)
link.insert(30)
link.insert(40)
link.insert(50)
link.print_all()
print("Size is: ", link.list_size())
print("remove")
# link.remove(10)
# link.remove(50)
link.remove(70)

print("Size is: ", link.list_size())
# link.remove(50)
# link.remove(30)
# link.remove(40)
# link.remove(20)


link.print_all()