'''
Given a binary tree with a value associated with each node. Your task is to select a subset of nodes such that the sum of their values is maximized, with the condition that no two selected nodes are directly connected that is, if a node is included in the subset, neither its parent nor its children can be included.

Examples:

Input: root[] = [11, 1, 2]

Output: 11
Explanation: The maximum sum is obtained by selecting the node 11.

Input: root[] = [1, 2, 3, 4, N, 5, 6]

Output: 16
Explanation: The maximum sum is obtained by selecting the nodes 1, 4, 5, and 6, which are not directly connected to each other. Their total sum is 16.  

Constraints:
1 ≤ no. of nodes in the tree ≤ 104
1 ≤ Node.val ≤ 105
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

def solve(root):
    if root is None:
        return 0
    
    inc = root.data
    if root.left:
        inc += solve(root.left.left) + solve(root.left.right)

    if root.right:
        inc += solve(root.right.left) + solve(root.right.right)
    
    exc = 0
    if root.left:
        exc += solve(root.left)
    if root.right:
        exc += solve(root.right)
    return max(exc, inc)

def maxAdjecent(root):
    return solve(root)

n = Node(11)
n.left = Node(1)
n.right = Node(2)

print(maxAdjecent(n))