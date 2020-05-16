#-------------------------------------------------------------------------------
# Name:        heapPriorityQueue
# Purpose:     This is an implementation of Binary Heap Priority Queue class.
#
# Author:      Armela Ligori
#
# Created:     16/05/2020
#-------------------------------------------------------------------------------
import math

class heapPriorityQueue:
    ''' A min-oriented priority queue implemented with a binary heap.'''
    def __init__(self):
        self.data = []         # Create a new empty priority queue

    def __len__(self):
        # Return the number of items in the priority queue
        return len(self.data)

    def parent(self, j):
        # Return the index of the parent of child at index j
        return (j - 1)//2

    def left(self, j):
        # Return the index of the left child of parent at index j (if any)
        if self.hasLeft(j):
            return 2 * j + 1

    def right(self, j):
        # Return the index of the right child of parent at index j (if any)
        if self.hasRight(j):
            return 2 * j + 2

    def hasLeft(self,j):
        if 2 * j + 1 <= len(self.data) - 1 :  # If left index exists,
            return True                       # there is a left child.
        else:                                 # If not,
            return False                      # there isn't.

    def hasRight(self,j):
        if 2 * j + 2 <= len(self.data) - 1 :  # If right index exists
            return True                       # there is a right child.
        else:                                 # If not,
            return False                      # there isn't

    def swap(self, i, j):
        # Swap the elements at indices i and j of array
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self,j):
        parent = self.parent(j)   # Get index of parent
        if parent < 0 :           # If root is reached,
            return                # End recursion
        else:
            if self.data[parent] > self.data[j] : # if parent greater than child
                self.swap(parent,j)               # swap values
                return self.upheap(parent)        # recur at position of parent

    def downheap(self, j):
        if self.hasLeft(j):
            # it cannot have right without having left so necessary to check only
            # for left to conclude it has children
            left = self.left(j)                   # get left child's index
            leftvalue = self.data[left]           # get left child's value
            if self.hasRight(j):                  # check if it has right
                right = self.right(j)             # get right child's index
                rightvalue = self.data[right]     #get right child's value

                if leftvalue <= rightvalue:       # find minimum value and index
                    minindex = left
                    minvalue = leftvalue
                else:
                    minindex = right
                    minvalue = rightvalue
            else:                       # if there is no right child (only left)
                minindex = left         # then index of min is index of left
                minvalue = leftvalue    # min value is left child's value

            if minvalue < self.data[j]: # comparing minimum of children to parent
                self.swap(j, minindex)  # swap if parent greater than min
            return self.downheap(minindex)   # recursive call at position of minimum child
        else:         # if no more children
            return    # end recursion

    def add(self,value):
        '''add a value to the priority queue'''
        self.data.append(value)         # Append to the end
        self.upheap(self.__len__()-1)   # Bubble up if it is smaller

    def min(self):
        '''return but do not remove minimum value.'''
        return self.data[0]             # minimum is first

    def removeMin(self):
        self.swap(0,(len(self.data)-1))   # swap first and last element
        min = self.data.pop()             # pop last element (which is min)
        self.downheap(0)                  # re-order elements
        return min

    def heightHeap(self):
        ''' return the height of the Heap'''
        return int(math.log2(self.__len__()))

    def k_smallestElement(self, k):
        ''' return k smallest element from the Heap in increasing order'''
        e = []    # will store smallest elements
        for i in range(k):
            e.append(self.removeMin())    # remove min elements k times
        return e                          # return list e

    def k_largestElement(self, k):
        ''' return k largest element from the Heap in decreasing order'''
        e = []
        maxHeap = heapPriorityQueue()     # create a new heap
        for i in self.data:
            maxHeap.add((-1)*i)     # add all elements but with a negative sign
            # the order from smallest to greates will reverse
        for i in range(k):          # append first k elements to e, which are min
            e.append((-1) * (maxHeap.removeMin()))  # but in revverse sign are max
        return e                    # return e
