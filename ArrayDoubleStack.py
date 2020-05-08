#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kostandin
#
# Created:     23/04/2020
# Copyright:   (c) Kostandin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class DoubleStack:
    DEFAULT_LEN = 4

    def __init__(self):
        self.data = [None]*self.DEFAULT_LEN
        self.sizeR = 0
        self.sizeB = 0
        self.frontB = len(self.data)//2

    def __lenR__(self):
        return self.sizeR

    def __lenB__(self):
        return self.sizeB

    def isEmptyR(self):
        return self.sizeR == 0

    def isEmptyB(self):
        return self.sizeB ==0

    def pushR(self, e):
        # Computing the index of the new R element
        index = self.sizeR
        if self.sizeR == self.frontB:
              self.resize(len(self.data)*2)
        self.data[index] = e
        self.sizeR += 1
        print(self.data)

    def pushB(self, e):
        # Computing the index of the new B element
        index = (self.frontB + self.sizeB )%len(self.data)
        if index == 0: # if the end is reached
            self.resize(len(self.data)*2)
        index = (self.frontB + self.sizeB )%len(self.data)
        self.data[index] = e
        self.sizeB += 1
        print(self.data)

    def resize(self, newCapacity):
        old = self.data
        self.data = [None] * newCapacity
        for i in range(self.sizeR):
            self.data[i] = old[i]
        walk = self.frontB
        for k in range(self.sizeB):
            self.data[newCapacity//2 + k] = old[walk]
            walk += 1
        self.frontB = newCapacity//2

    def popR(self):
        if self.isEmptyR():
            print('Red Stack is empty')
        else:
            e = self.data[self.sizeR-1]
            self.data[self.sizeR-1] = None
            self.sizeR -= 1
            print(self.data)
            return e

    def popB(self):
        if self.isEmptyB():
            print('Blue Stack is empty')
        else:
            e = self.data[self.frontB + self.sizeB - 1]
            self.data[self.frontB + self.sizeB - 1] = None
            self.sizeB -= 1
            print(self.data)
            return e

    #top r and top b

ds = DoubleStack()
ds.pushR(2)
ds.pushB(1)
ds.pushR(4)
ds.pushR(3)
print(ds.popR())
ds.pushB(67)
ds.pushB(3)
print(ds.popB())

