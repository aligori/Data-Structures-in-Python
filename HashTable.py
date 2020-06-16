#-------------------------------------------------------------------------------
# Name:        Hash Table implementation
# Purpose:     This is a hash table implementation using linear probing.
#
# Author:      Armela Ligori
#
# Created:     01/06/2020

#-------------------------------------------------------------------------------

hashTable = [(None, None) for i in range(10)]

def hashFuncKey(data, key):
    return key % len(data)

def insert(data, key, value):
    hashKey = hashFuncKey(data, key)
    keyExists = False
    for i in range(len(data)):
        # getting key and value of the hashkey index ( + i for linear probing)
        k, v = data[(hashKey + i)%len(data)]
        if k == key:          # Checking if key exists
            keyExists = True  # setting status to true
            break             # if so breaking the loop
        elif k == None:       # if key becomes None, no need to continue with -
            break             # the rest of the loop since we started from hashKey index

    if  keyExists :
        data[(hashKey + i)%len(data)] = (key, value)
    else:
        for i in range(len(data)): # Finding free spot
            k, v = data[(hashKey + i)%len(data)]
            if  k == None or k == 'deleted':
                data[(hashKey + i)%len(data)] = (key, value)
                break

def delete(data, key):
    hashKey = hashFuncKey(data, key)     # Get hashkey index
    keyExist = False
    for i in range(len(data)):
        # getting key and value of the hashkey index ( + i for linear probing)
        k, v = data[(hashKey + i)%len(data)]

        if k == key:   # key is found
            keyExist = True
            break
        elif  k == None:
            break
            '''If k becomes None it means the key we are searching for, doesn't
            exist. There is no need to continue the loop. Since we are starting
            from the hashkey index , then if our key is present it will be before
            None is reached'''

    if keyExist :     # if key is found
        data[(hashKey + i)%len(data)] = ('deleted','deleted') # rename tuple as deleted
    else:
        print('Not Found')    # else print not found

def search(data, key):
    hashKey = hashFuncKey(data, key)     # Get hashkey index
    keyExist = False


    if data[hashKey] != (None,None):   # If key at hashkey index is None, it is obvious that what we are looking for, is not there
                                       # However if it is deleted the loop will execute
        for i in range(len(data)):
            k, v = data[(hashKey + i)%len(data)]  # we get the key and value starting from hashkey index
            if k == key:  # if current key is equal to the key we are looking for
                keyExist = True  # then key is found
                break

    if keyExist :
        print( data[(hashKey + i)%len(data)][1] ) # getting the value if the key was found
    else:
        print( 'Key Not Found')   # else printing key not found


insert(hashTable, 10, 'Alex')
insert(hashTable, 14, 'Mary')
insert(hashTable, 18, 'Deni')
insert(hashTable, 20, 'Jane')
insert(hashTable, 21, 'Besmir')
insert(hashTable, 30, 'Kejd')
insert(hashTable, 24, 'Rei')
insert(hashTable, 18, 'Rei')
print(hashTable,'\n')

delete(hashTable, 10)
print(hashTable)

search(hashTable, 20)
insert(hashTable, 10, 'Martin')
print(hashTable)
search(hashTable, 20)