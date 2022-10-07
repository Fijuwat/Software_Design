class Stack(object):

    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        if (not self.isEmpty()):
            return self.stack.pop()
        else:
            return None

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    # a string representation of this stack.
    def __str__(self):
        return str(self.stack)


class Queue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        return self.stack1.__str__()

    def enqueue(self, firstthing):
        if self.stack1.isEmpty():
            self.stack1.push(firstthing)
        else:
            while (not self.stack1.isEmpty()):
                self.stack2.push(self.stack1.pop())
            self.stack1.push(firstthing)
            for i in range(self.stack2.size()):
                self.stack1.push(self.stack2.pop())


    def dequeue(self):
        return self.stack1.pop()




###############################
#                             #
#   Example run of a Queue    #
#                             #
###############################


my_queue = Queue()

# enqueue 10
my_queue.enqueue(10)
print(my_queue)

# enqueue 18
my_queue.enqueue(18)
print(my_queue)


# enqueue 1024
my_queue.enqueue(1024)
print(my_queue)


# dequeue()
print("Dequeue ", my_queue.dequeue())
print("Dequeue ", my_queue.dequeue())
print("Dequeue ", my_queue.dequeue())
print("Dequeue ", my_queue.dequeue())
