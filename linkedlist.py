class Link():
    ''' This class represents a link between data items only'''

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


class LinkedList():
    ''' This class implements the operations of a simple linked list'''

    def __init__(self):
        self.first = None

    def insertFirst(self, data):
        '''insert data at begining of a linked list'''
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    def insertLast(self, data):
        ''' Insert the data at the end of a linked list '''
        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            return
        # find the last and insert it there.
        while (current.next != None):
            current = current.next

        current.next = newLink

    def findLink(self, data):
        ''' find to which data is the link of a given data inside this linked list'''
        current = self.first
        if (current == None):
            return None

        # searcg and find the position of the given data, the get the link if.
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    def deleteLink(self, data):
        ''' Removes the data from the list if exist and fix the link problems.'''

        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current

            current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    def __str__(self):
        return str(self.first)


class Stack(object):

    def __init__(self):
        self.ll = LinkedList()

    # add an item to the top of the stack
    def push(self, item):
        self.ll.insertFirst(item)

    # remove an item from the top of the stack
    def pop(self):
        if self.ll.first == None:
            return None
        else:
            data = self.ll.first.data
            return self.ll.deleteLink(data).data

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.ll.first.data
    # check if a stack is empty
    def isEmpty(self):
        return self.ll.first == None

    # return the number of elements in the stack
    def size(self):
        n = 0
        current = self.ll.first

        while not current == None:
            current = current.next
            n += 1
        return n


    # a string representation of this stack.
    def __str__(self):
        return self.ll.__str__()



###############################
#                             #
#   Example run of a stack    #
#                             #
###############################

my_stack = Stack()

print(my_stack.size())
# Push 10
my_stack.push(10)
print(my_stack)
print(my_stack.size())
# Push 18
my_stack.push(18)
print(my_stack)
print(my_stack.size())
# Push 1024
my_stack.push(1024)
print(my_stack)
print(my_stack.size())
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
