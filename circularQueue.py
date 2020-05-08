#-------------------------------------------------------------------------------
# Name:        circularQueue
# Purpose:     This is the implementation of a Queue class, using a circularly
#              linked list as storage.
#
# Author:      Armela Ligori
#
# Created:     27/04/2020
#-------------------------------------------------------------------------------

class circularQueue:

    class Node:
        __slots__ = 'element','next'       # streamline memory usage
        def __init__(self, element, next): # initialize node's fields
            self.element = element         # reference to user's element
            self.next = next               # reference to next node

    def __init__(self):              # Create an emptyy Queue
        self.tail = None             # will represent tail of queue
        self.size = 0                # number of nodes in queue

    def len(self):
        return self.size             # return the size of the queue

    def is_Empty(self):
        return self.size == 0        # returns true if queue is empty

    def first(self):
        if self.is_Empty():          # checking if queue is empty
            return 'Queue is empty'  # if it is then return that it is empty
        head = self.tail.next        # tail.next points to head
        return head.element          # return first element

    def dequeue(self):
        # Remove and return the first element
        if self.is_Empty():          # checking if queue is empty
            return 'Queue is empty'  # there is nothing to dequeue
        oldhead = self.tail.next     # keeping a reference to the current head
        if self.size == 1:           # removing the only element
            self.tail = None         # queue becomes empty
        else:
            self.tail.next = oldhead.next   # bypass the old head
        self.size -= 1                      # decrement the size of queue
        return oldhead.element              # return the removed element

    def enqueue(self, e):
        newest = self.Node(e, None)     # node will be new tail node
        if self.is_Empty():             # If queue is empty:
            newest.next = newest        # initialize circularly, points to self
        else:
            newest.next = self.tail.next    # new node points to head
            self.tail.next = newest         # old tail points to new node
        self.tail = newest                  # new node becomes the tail
        self.size += 1                      # increment size of queue

    def rotate(self):
        # Rotate front element to the back of the queue.
        if self.size > 0:
            self.tail = self.tail.next      # old head becomes new tail

    def display(self):
        if self.is_Empty():                 # If queue is empty
            return 'Queue is empty'         # there is nothing to display
        itrNode = self.tail                 # make a new reference to tail

        while(itrNode.next != self.tail):   # checking if we returned to tail
            # printing current next element (first will be head)
            print(itrNode.next.element, ' -> ', end = " ")
            itrNode = itrNode.next          # itrNode points to next element

        # while loop was exited before printing tail element
        print(itrNode.next.element, ' -> ', end = " ") # printing tail element
        print('\n')
