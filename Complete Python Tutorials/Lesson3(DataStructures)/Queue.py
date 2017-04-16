class Queue():
    def __init__(self):
        self.queue = []                         # start with empty queue

    def isEmpty(self):
        return self.queue == []                 # return empty

    def enqueue(self, data):
        self.queue.insert(0,data)               # built in insert to enqueue the data

    def dequeue(self):
        return self.queue.pop()                 # remove the data

    def m_size(self):
        return len(self.queue)                  # return length of queue as list

    def print_all(self):
        for each in self.queue:
            print(each)

que = Queue()

que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
print(que.m_size())
print(que.dequeue())
print(que.dequeue())
print(que.isEmpty())


