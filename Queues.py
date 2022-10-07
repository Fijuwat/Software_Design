class Queue(object):
    '''Queue implements the FIFO principle.'''

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if (not self.isEmpty()):
            return self.queue.pop()
        else:
            return None

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    # a string representation of this stack.
    def __str__(self):
        return str(self.queue)


class Stack(object):

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    # add an item to the top of the stack
    def push(self, item):
        if self.queue1.isEmpty():
            self.queue1.enqueue(item)
        else:
            self.queue2 = self.queue1
            self.queue1 = Queue()
            self.queue1.enqueue(item)
            while not self.queue2.isEmpty():
                self.queue1.enqueue(self.queue2.dequeue())


    # remove an item from the top of the stack
    def pop(self):
        return self.queue1.dequeue()
    # check what item is on top of the stack without removing it
    def peek(self):
        if self.queue1.isEmpty():
            return None
        else:
            self.queue2 = self.queue1
            element = self.queue2.dequeue()
            self.queue2 = Queue()
            return element
    # check if a stack is empty
    def isEmpty(self):
        return self.queue1.isEmpty()

    # return the number of elements in the stack
    def size(self):
        return self.queue1.size()

    # a string representation of this stack.
    def __str__(self):
        return self.queue1.__str__()

###############################
#                             #
#   Example run of a stack    #
#                             #
###############################

my_stack = Stack()

# Push 10
my_stack.push(10)
print(my_stack)

# Push 18
my_stack.push(18)
print(my_stack)

# Push 1024
my_stack.push(1024)
print(my_stack)

# pop()
print("pop()  ", my_stack.pop())

# peek()
print("peak()  ", my_stack.peek())

# isEmpty()
print("isEmpty()   ", my_stack.isEmpty())

print("pop()  ", my_stack.pop())
print("pop()  ", my_stack.pop())
print("pop()  ", my_stack.pop())
print("isEmpty()   ", my_stack.isEmpty())
