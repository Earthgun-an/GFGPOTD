'''
You are given a binary tree, and the task is to determine whether it satisfies the properties of a max-heap.

A binary tree is considered a max-heap if it satisfies the following conditions:

Completeness: Every level of the tree, except possibly the last, is completely filled, and all nodes are as far left as possible.
Max-Heap Property: The value of each node is greater than or equal to the values of its children.
Examples:

Input: root[] = [97, 46, 37, 12, 3, 7, 31, 6, 9]
 
Output: true
Explanation: The tree is complete and satisfies the max-heap property.
Input: root[] = [97, 46, 37, 12, 3, 7, 31, N, 2, 4] 
 
Output: false
Explanation: The tree is not complete and does not follow the Max-Heap Property, hence it is not a max-heap.
'''

from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def isHeap(root):
    if root is None:
        return True
    q = deque()
    q.append(root)
    nullNode = False
    while q:
        node = q.popleft()
        if node.left:
            if nullNode or node.data < node.left.data:
                return False
            q.append(node.left)
        else:
            nullNode = True
        if node.right:
            if nullNode or node.data > node.right.data:
                return False
            q.append(node.right)
        else:
            nullNode = True
    return True

n = Node(97)
n.left = Node(46)
n.right = Node(37)
n.left.left = Node(12)
n.left.right = Node(3)
n.left.left.left = Node(6)
n.left.left.right = Node(9)
n.right.left = Node(7)
n.right.right = Node(31)

print(isHeap(n))