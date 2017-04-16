class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def sizeTwo(self):
        return self.size

    def size2(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        print(size)

    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d" %actualNode.data)
            actualNode = actualNode.nextNode

    def remove(self, data):
        if self.head is None:
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


linklist = LinkedList()

# linklist.insertStart(12)
# linklist.insertStart(22)
# linklist.insertStart(32)
# linklist.insertStart(42)
# linklist.insertStart(52)
# linklist.insertStart(62)
# linklist.insertEnd(112)
# linklist.insertStart(72)
# linklist.insertStart(82)
# linklist.insertEnd(212)
# linklist.traverseList()
# linklist.size2()

linklist.insertStart(10)
linklist.traverseList()
print("remove")
linklist.remove(10)
linklist.size2()
linklist.traverseList()