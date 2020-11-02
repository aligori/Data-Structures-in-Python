#-------------------------------------------------------------------------------
# Name:        SinglyQueue
# Purpose:     This is an implementation for Queue Class using  a Singly Linked
#              List as storage.
#
# Author:      Armela Ligori
#
# Created:     27/04/2020
#-------------------------------------------------------------------------------

class SinglyQueue:

    class Node:
        __slots__ = 'element','next'       # streamline memory usage
        def __init__(self, element, next): # initialize node's instance variables
            self.element = element         # reference to user's element
            self.next = next               # reference to next node

    def __init__(self):     # Create an empty queue
        self.head = None    # reference to the head node
        self.tail = None    # reference to the tail node
        self.size = 0       # number of elements in queue

    def len(self):
        return self.size    # return the size of the queue

    def is_Empty(self):
        return self.size == 0   # check if queue is empty

    def first(self):
        if self.is_Empty():          # Check if queue is empty
            return 'Queue is empty'  # if it is, return that it is empty
        return self.head.element     # return the first element in queue

    def dequeue(self):
        # Remove and return the first element of a queue
        if self.is_Empty():          # check if queue is empty
            return 'Queue is empty'  # if true then return that it is empty
        answer = self.head.element   # answer holds the first element in queue
        self.head = self.head.next   # make head variable point to next node
        self.size -= 1               # decrement size
        if self.is_Empty():          # special case as queue becomes empty
            self.tail = None         # the removed head, had been the tail
        return answer                # return first element removed from queue

    def enqueue(self, e):
        # Add an element to the back of the queue
        new = self.Node(e, None)     # Create a new node containing a reference
                                     # to new element and a reference to None

        if self.is_Empty():          # special case: previously empty
            self.head = new          # then head will reference newest node
        else:                        # if not previously empty then:
            self.tail.next = new     # current tail node will reference newest
        self.tail = new              # set variable tail to reference new node
        self.size += 1               # increment node count (queue size)

    def display(self):               # Displays the whole queue
        itrNode = self.head          # Make a new reference to head, so we won't
                                     # lose reference to first element after
                                     # traversing the linked list.

        if self.is_Empty():          # if queue is empty
            return 'Queue is empty'  # return that it is empty
        while(itrNode != None):      # we'll go to each node until we reach None
            print(itrNode.element, ' -> ', end = " ")  # Print current element
            itrNode = itrNode.next   # change itrNode's reference to point to
                                     # next element
