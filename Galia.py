#!/bin/python3

import sys
import itertools
from fractions import Fraction



class BST:
    children = []
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
        BST.children.append(val)

def binary_insert(root, node):
    if root is None:
        root = node
    else:


        if root.data > node.data:
            if root.left is None:
                root.left = node
                if root.data in BST.children:
                    BST.children.remove(root.data)
            else:
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                if root.data in BST.children:
                    BST.children.remove(root.data)
            else:
                binary_insert(root.right, node)

    #print(BST.children)

def create_BST(numbers):
    BST.children = []
    root = BST(numbers[0])
    #print(numbers , BST.children)


    for i in range(1, len(numbers)):
        binary_insert(root, BST(numbers[i]))

    return sum(BST.children)

def expectedAmount(a):
    # Complete this function
    a = set(itertools.permutations(a))
    #print(a)
    l = len(a)
    sum = 0
    for x in a:
        sum += create_BST(x)

    print(Fraction(sum, l))



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        expectedAmount(a)
