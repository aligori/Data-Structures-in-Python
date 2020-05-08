#-------------------------------------------------------------------------------
# Name:        ArrayDeque
# Purpose:     The purpose of this program is to provide an Array-Based
#              Implementation  of collections.deque class and its most used
#              functions.
#
# Author:      Armela Ligori
#
# Created:     23/04/2020
# Last edited: 30/04/2020
#-------------------------------------------------------------------------------

class ArrayDeque:
    DEFAULT_CAPACITY = 4  # Default capacity of underlying list

    def __init__(self, maxlen = None):
        self.data = [None]*self.DEFAULT_CAPACITY   # underlying list
        self.size = 0         # current number of elements stored in deque
        self.front = 0        # the index of the first element in deque
        self.back = -1        # the index of the last element in deque
        self.maxlen = maxlen  # optional parameter to force a fixed-length deque

    def len(self):
        return self.size       # Return the size of deque

    def isEmpty(self):
        return self.size == 0  # Check if there are no elements in the Deque

    def append(self, e):
        # Adding a new element to the back of the deque (Back index will change)

        if self.size == len(self.data):         # if the underlying list is full
                self.resize(2 * len(self.data)) # attempt to resize

        pos = (self.back + 1)%len(self.data)    # Position after back
        self.data[pos] = e                      # add element to that position
        self.back = pos                         # change back to point to the
                                                # new last element

        if self.maxlen is not None and self.size == self.maxlen:
            # if this condition is true, the underlying list was not resized
            # an element is lost at the front, self.size remains the same
            self.front = (self.front + 1)%len(self.data) # change front
        else:
            self.size += 1  # number of elements in deque is increased


    def appendleft(self,e):
        # Adding a new element at the beginning of the Deque (Front will change)

        if self.size == len(self.data):         # if the underlying list is full
                self.resize(len(self.data)*2)   # attempting to resize

        pos = (self.front - 1)%len(self.data)   # position before front
        self.data[pos] = e                      # add element to that position
        self.front = pos                        # change front to point to the
                                                # new added first element

        if self.maxlen is not None and self.size == self.maxlen:
            # the underlying list was not resized, max number of elements in
            # deque is reached, so self.size won't change. An element is lost
            # at the back so self.back needs to point to back - 1
            self.back = (self.back - 1)%len(self.data)
        else:
            self.size += 1                      # increase size of deque



    def resize(self, capacity):

        if self.maxlen is not None and self.size < self.maxlen : # if maxlen not reached
            if capacity >  self.maxlen:         # if capacity exceeds maxlen
                capacity = self.maxlen          # at least resize to maxlen
        elif self.size == self.maxlen:          # if maxlen reached
            return    # no  need to create the same array again so skip the rest

        old = self.data                 # Keep track of the existing list
        self.data = [None]*capacity     # Allocate a list with new capacity
        walk = self.front               # Will be used to walk through all
                                        # elements of queue in old list

        for k in range(self.size):             # Consider only existing elements
            self.data[k] = old[walk]           # Intentionally shift indices
            walk = (walk + 1) % len(old)       # Using old size as modulus
        self.front = 0                         # front has been realigned
        self.back = k                          # back has been realigned

    def pop(self):
        # Remove last element of deque (Back index will change)

        if self.isEmpty():
            return 'Deque Empty'               # No item to pop

        e = self.last()                        # Get the last element in deque
        self.data[self.back] = None            # set the reference to None
        self.size -= 1                         # Size is decreased by 1
        self.back = (self.back - 1) % len(self.data)    # Change back index
        return e                                        # Return the element

    def popleft(self):
        # Remove first element of the deque (Front index will change)

        if self.isEmpty():
            return 'Deque Empty'               # No item to pop

        e = self.first()                       # Get the first element in deque
        self.data[self.front] = None           # set the reference to None
        self.size -= 1                         # Size is decreased by 1
        self.front = (self.front + 1 ) % len(self.data)  # Change front index
        return e                                         # Return the element

    def first(self):
        if self.isEmpty():                     # Check if empty
            return 'Deque is empty'
        return self.data[self.front]           # Return first element

    def last(self):
        if self.isEmpty():                     # Check if empty
            return 'Deque is empty'
        return self.data[self.back]            # Return last element

    def get(self, i):
        # get element which is i positions after front
        if i < 0 or i >= self.size:
            'Incorrect index'
        return self.data[(self.front + i) % len(self.data)]

    def set(self, i, value):
        # set a new value for element at position i after front
        if i < 0 or i >= self.size:
            'Incorrect index'
        self.data[(self.front + i) % len(self.data)] = value

    def clear(self):
        self.data = [None] * len(self.data)   # Set data to point to a new array
        self.front = 0                        # Reinitalize front
        self.back = -1                        # Reinitialize back
        self.size = 0                         # Size of deque is 0

    def remove(self, value):
        index = None                     # if index won't change, 2nd loop will
                                         # not be executed

        for i in range(self.size):       # for all the values in deque
            ans = self.popleft()         # we pop the current value
            if ans == value:             # if it is the required value
                index = i                # keep track of index where it is found
                break                    # break the loop, don't append element
            else:
                self.append(ans)         # if it's not the required value
                                         # append the element again to deque

        if index is None:                    # if value not found,
            return 'Value not found'         # return from the function
                                             # following loop won't be executed

        for i in range(index,self.size):     # for the remaining values
            ans = self.popleft()             # pop element from the left
            self.append(ans)                 # append to the back
        # in this way the order of the remaining elements will remain the same

    def rotate(self, k):
        # pop k elements from the right and append them to the left
        for i in range(k):
            e = self.pop()                   # pop from the right
            self.appendleft(e)               # append to the left

    def count(self,value):
        cnt = 0                                     # initialize counter with 0
        for i in range(self.size):                  # i from 0 to self.size
            if self.data[(self.front + i) % len(self.data)] == value:  # if true
                cnt +=1                             # increment the counter
        return cnt                                  # return the counter
