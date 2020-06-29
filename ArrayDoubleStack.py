#-------------------------------------------------------------------------------
# Name:        ArrayDoubleStack.py
# Purpose:     This program implements a Color-Coded Double Stack. Based on the
#              order in which we place the RED and BLUE elements, 2 different
#              approaches are used. There are 2 classes: DoubleStackHalf, which
#              devides the array space into two halves, one for each color; and
#              DoubleStack class which uses the second approach and places the
#              red elements and blue elements starting from opposite ends.
#
# Author:      Armela Ligori
#
# Last Edited: 24/06/2020
#-------------------------------------------------------------------------------

''' This class uses the first approach for implementing the Double Stack
    Red and blue stacks within the array have pre-defined sizes. They can occupy
    only half of the current array size'''

class DoubleStackHalf:
    DEFAULT_LEN = 4

    def __init__(self):
        self.data = [None]*self.DEFAULT_LEN    # Initialize underlying array
        self.sizeRed = 0                       # Number of red elements
        self.sizeBlue = 0                      # Number of blue elements
        self.frontBlue = len(self.data)//2     # Points to beginning of blue stack

    def lenR(self):
        return self.sizeRed                    # Return size of red stack

    def lenB(self):
        return self.sizeBlue                   # Return size of blue stack

    def isEmptyR(self):
        return self.sizeRed == 0               # Check if there are red elements

    def isEmptyB(self):
        return self.sizeBlue == 0              # Check if there are blue elements

    def pushR(self, e):                        # Push a red element in the stack

        index = self.sizeRed                   # The index of the new R element
        if self.sizeRed == self.frontBlue:     # If half of the array is reached,
              self.resize(len(self.data)*2)    # resize underlying array
        self.data[index] = e                   # Place red element at index
        self.sizeRed += 1                      # Increment size of red

    def pushB(self, e):                       # Push a blue element in the stack
        # Computing the index of the new B element
        index = (self.frontBlue + self.sizeBlue )
        if index == len(self.data):                   # If the end is reached,
            self.resize(len(self.data)*2)             # resize underlying array
            index = (self.frontBlue + self.sizeBlue ) # Re-calculate next top index
                                                      # for blue if array is resized
        self.data[index] = e        # Place new element into calculated index
        self.sizeBlue += 1          # Increment size of blue stack

    def resize(self, newCapacity):
        old = self.data                     # keep a reference to old array
        self.data = [None] * newCapacity    # Allocate an array with new capacity

        for i in range(self.sizeRed):       # Start copying all red elements
            self.data[i] = old[i]           # starting from the beginning of array

        walk = self.frontBlue               # Will be used to walk through all blue
                                            # elements of old stack
        for k in range(self.sizeBlue):      # Consider only existing blue elements
            # Copy elements starting from half of the array
            self.data[newCapacity//2 + k] = old[walk]
            walk += 1
        self.frontBlue = newCapacity//2     # Front of blue has been re-aligned

    def popR(self):                           # Pop last red element (LIFO)
        if self.isEmptyR():                   # Check if there are any red elements
            print('No red element in stack')  # Return message
        else:
            e = self.topR()                   # Get the last red element
            self.data[self.sizeRed-1] = None  # Set reference to None
            self.sizeRed -= 1                 # Decrement Number of red elements
            return e                          # Return last red element

    def popB(self):                           # Pop last blue element (LIFO)
        if self.isEmptyB():                   # Check if there are any blue elements
            print('No Blue elements')         # Return message
        else:
            e = self.topB()                   # Get the last blue element
            # Set reference of top index to None
            self.data[self.frontBlue + self.sizeBlue - 1] = None
            self.sizeBlue -= 1                # Decrement number of blue elements
            return e                          # Return last blue element

    def topR(self):
        # Calculate index of top Red element and return it
        return self.data[self.sizeRed-1]

    def topB(self):
        # Calculate index of top Blue element and return it
        return self.data[self.frontBlue + self.sizeBlue - 1]

    def displayData(self):
        # Display all info related to both colored stacks
        print('Double Stack: ',self.data,' size of Red: ',self.sizeRed,' Top Red element: ',self.topR(),
              ' size of Blue: ',self.sizeBlue,' Top Blue element: ',self.topB())


#-------------------------------------------------------------------------------


''' This class uses the second approach for implementing the Double Stack
    Elements are pushed starting from opposite ends of the array'''

class DoubleStack:
    DEFAULT_LEN = 4

    def __init__(self):
        self.data = [None]*self.DEFAULT_LEN   # Initialize underlying array
        self.sizeR = 0                        # Size of red elements
        self.sizeB = 0                        # Size of blue elements

    def pushR(self, e):
        # Computing the index of the new R element
        # since top = sizeR - 1, we have top + 1 = sizeR
        index = self.sizeR
        # Overflow occurrs only when array becomes full (top of red is before
        # top of blue.
        if self.sizeR + self.sizeB == len(self.data): # Check if overflow occurrs,
              self.resize(len(self.data)*2)           # resize to twice capacity
        self.data[index] = e                          # Add new element at top index
        self.sizeR += 1                               # Increment red size

    def pushB(self, e):
        # Overflow occurrs when top of blue 'meets' top of red. This only happens
        # if the underlying array is full
        if self.sizeR + self.sizeB == len(self.data): # Check for overflow
            self.resize(len(self.data)*2)             # Resize to twice capacity

        # Calculate new top index : New blue element should be placed starting -
        # from the end index minus current number of elements
        index = (len(self.data) - self.sizeB - 1)
        self.data[index] = e          # Add new element to calculated index
        self.sizeB += 1               # Increment number of blue elements

    def resize(self, newCapacity):
        old = self.data               # Keep reference of old array
        self.data = [None] * newCapacity  # Allocate new array

        for i in range(self.sizeR):   # Copy all red elements,
            self.data[i] = old[i]     # starting from the beginning

        # walk Will be used to walk through all blue elements of old array,
        # starting from the front of blue stack which is actually end of the old array.
        walk = len(old) - 1

        for k in range(self.sizeB):                      # For each blue element,
            self.data[len(self.data)-1-k] = old[walk]    # copy it starting from end of new array
            walk -= 1                                    # Decrement index of blue element

    def popR(self):                           # Remove and return last red element
        if self.isEmptyR():                   # Check if there are red elments
            print('No red elements')          # Return message
        else:
            e = self.topR()                   # Get top red element
            self.data[self.sizeR-1] = None    # Set top reference to None
            self.sizeR -= 1                   # Decrement number of red elements
            return e                          # Return last red element

    def popB(self):                           # Remove and return last blue element
        if self.isEmptyB():                   # Check if there are any blue elements
            print('No Blue elements')         # Return message if there aren't
        else:
            e = self.topB()                   # Get top blue element
            self.data[len(self.data)-self.sizeB] = None  # Set reference to None
            self.sizeB -= 1                   # Decrement size of blue
            return e                          # Return last blue element

    def lenR(self):
        return self.sizeR                     # Return number of red elements

    def lenB(self):
        return self.sizeB                     # Return number of blue elements

    def isEmptyR(self):
        return self.sizeR == 0                # Check if there are any red elem.

    def isEmptyB(self):
        return self.sizeB ==0                 # Check if there are any blue elem.

    def topR(self):
        if self.isEmptyR():                   # Check if there are red elments
            return('No red elements')         # Return message if there aren't
        return self.data[self.sizeR-1]        # Return top of red stack

    def topB(self):
        if self.isEmptyB():                   # Check if there are any blue elements
            return('No Blue elements')        # Return message if there aren't
        return self.data[len(self.data)-self.sizeB]  # Return top of blue stack

    def displayData(self):
        # Display all info related to both colored stacks
        print('Double Stack: ',self.data,' size of Red: ',self.sizeR,' Top Red element: ',self.topR(),
              ' size of Blue: ',self.sizeB,' Top Blue element: ',self.topB())
