#-------------------------------------------------------------------------------
# Name:        MergeSort
# Purpose:     This is an implementation for Merge sort algorithm.
#
# Author:      Armela Ligori
#
# Created:     09/06/2020
#-------------------------------------------------------------------------------
import random

def mergeSort(A):
    if len(A) ==  1:
        return A
    # divide
    middle = len(A)//2              # finding the middle index
    # Conquer
    left = mergeSort(A[:middle])    # apply mergeSort in left half
    right = mergeSort(A[middle:])   # apply mergeSort in right half
    # Merging results
    return merge(left, right)


def merge(left, right):
    C = [None]*(len(left) + len(right))   # New space allocated for merged array
    i = 0   # Pointer to elements of left array
    j = 0   # Pointer to elements of right array
    r = 0   # Pointer to elements of merged array
    while i < len(left) and j < len(right): # while we haven't reached the end of the arrays
        if left[i] < right[j]:   # compare current indexed element in left list with element in right list
            C[r] = left[i]       # if element in left is smaller add it to the merged list
            i += 1               # increment pointing index for left
            r += 1               # increment pointing index for merged array
        else:
            C[r] = right[j]      # else if right is smaller add it to the merged array
            j += 1               # increment pointing index for right array
            r += 1               # increment pointing index for merged array
    while i < len(left):         # if the end of the left array was not reached
        C[r] = left[i]           # add remaining elemements at the end of the merged array
        i += 1                   # increment pointing index to left array
        r += 1                   # increment pointing index to merged array
    while j < len(right):        # if the end of the right array was not reached
        C[r] = right[j]          # add remaining elemements at the end of the merged array
        j += 1                   # increment pointing index to right array
        r += 1                   # increment pointing index to merged array
    return C                     # return merged array