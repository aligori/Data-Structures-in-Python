#-------------------------------------------------------------------------------
# Name:        QuickSort
# Purpose:     This program provides an implementation of QuickSort Algorithm
#              using Haore Schema.
#
# Author:      Armela Ligori
#
# Created:     09/06/2020
#-------------------------------------------------------------------------------
import random
import time

def partition(A, l, r):
    pivot = A[l]  # pivot is the leftmost position of the subarray
    # print('Pivot: ',pivot)

    i = l   # i searches any element greater than pivot starting from the leftmost element
    j = r   # j searches any element smaller than pivot starting from the rightmost element

    while (i < j):
        while((A[i] <= pivot) and i < r):
            i += 1  # keep incrementing i until an element > pivot is found
        while((A[j] > pivot) and j > l):
            j -= 1  # keep decrementing j until an element < pivot is found
        if i < j:   # if index i hasn't surpassed j yet
            #print(A)
            A[i], A[j] = A[j], A[i]   # swap smaller element with larger
    # print(A)
    A[l], A[j] = A[j], A[l]   # swap pivot with element at position j (partitioning position)
    # print(A)
    return j  # return the partitioning position


def QuickSort(A, l, r):
    if (l < r):

        ''' Divide'''
        # pp = partition(A, l, r)       # Uncomment when Pivot first element
        pp = randomPivot(A, l, r)      # Uncomment when Pivot random element
        # pp = middlePivot(A, l, r)    # Uncomment when Pivot middle element
        # pp is partitioning position, A[pp] is now at the right place
        ''' Conquer '''
        QuickSort(A, l, pp-1)   # run quicksort for the left subarray
        QuickSort(A, pp+1, r)   # run quicksort for the right subarray

def randomPivot(A , l, r):
    # Generating a random number between the starting index of the subarray and
    # the ending index of the subarray.
    randpivot = random.randrange(l, r)

    # Swapping the leftmost element of the subarray and the randomly chosen element
    # so that when partition function is called, it will become the pivot
    A[l], A[randpivot] = A[randpivot], A[l]
    return partition(A, l, r)


def middlePivot(A, l, r):
    middle = (l+r)//2
    # Swapping the leftmost element of the subarray and the middle, so that
    # when we call partition method, the pivot will become the leftmost element
    # which will actually be the one that was in the middle.
    A[l], A[middle] = A[middle], A[l]
    return partition(A, l, r)

'''
# Driver Code - Testing for different pivoting options

N = [100, 1000, 10000, 100000, 1000000]

for n in N:
    # A = [i for i in range(n)]     # Pre-Sorted

    A = []
    for i in range(n):            # Random
        e = random.randint(1, n)
        A.append(e)

    start = time.time()
    QuickSort(A, 0, len(A)-1)
    time.sleep(1)
    finish = time.time()
    print('N = ',n,' Time: ',finish - start - 1)
# print('Sorted ',A)

'''

