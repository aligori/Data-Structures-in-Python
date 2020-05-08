#-------------------------------------------------------------------------------
# Name:        Binary Search Tree
# Purpose:     These are implementations of functions of Binary Search Trees.
#
# Author:      Armela Ligori
#
# Created:     08/05/2020
#-------------------------------------------------------------------------------

class BST:
    def __init__(self, value):             # Creating a new Node
        self.value = value
        self.left = None
        self.right = None

    def insertNode(self, value):           # Inserting node at the proper place

        if value <= self.value and self.left:
            # if node's value is greater than value and there is a left child
            self.left.insertNode(value)    # call the function for right child
        elif value <= self.value:          # When there is no more left child
            self.left = BST(value)         # insert the node
        elif value > self.value and self.right:
            # if node's value is smaller than value and there is a right child
            self.right.insertNode(value)   # call the function for right child
        else:
            self.right = BST(value)        # when there is no more right child
                                           # insert the node

    def preorder(self):
        print(self.value, end = ' ')       # Print the value of the node
        if self.left:                      # If it has left child,
            self.left.preorder()           # call function again for left child
        if self.right:                     # If it has right child
            self.right.preorder()          # call function again for right child

    def postorder(self):
        if self.left:                      # If it has left child,
            self.left.postorder()          # call function again for left child
        if self.right:                     # If it has right child,
            self.right.postorder()         # call function again for right child
        print(self.value, end = ' ')       # Print the value of the node

    def findMin(self):
        if self.left == None:     # If there is no more a left child
            return self.value     # Min value is the current value
        else:
            return self.left.findMin()   # if there is a left child,
                                         # we ge to the next left child

    def findMax(self):
        if self.right == None:    # If there is no more a right child
            return self.value     # Max value is the current value
        else:
            return self.right.findMax()   # if there are more right children,
                                          # we ge to the next right child

    def findNode(self, data):
        if self.value == data:                  # value is found
            return 1
        elif self.left and self.value > data:   # if data < self.value,
            return self.left.findNode(data)     # then the value might be in the left subtree
        elif self.right and self.value < data:  # if data > self.value,
            return self.right.findNode(data)    # then the value might be in the right subtree
        else:
            return 0                            # value not found

