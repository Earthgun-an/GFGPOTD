'''
You are given the root of a binary tree. Your task is to return the left view of the binary tree. The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.

If the tree is empty, return an empty list.

Examples :

Input: root[] = [1, 2, 3, 4, 5, N, N]

Output: [1, 2, 4]
Explanation: From the left side of the tree, only the nodes 1, 2, and 4 are visible.

Input: root[] = [1, 2, 3, N, N, 4, N, N, 5, N, N]

Output: [1, 2, 4, 5]
Explanation: From the left side of the tree, the nodes 1, 2, 4, and 5 are visible.

Input: root[] = [N]
Output: []
Constraints:
0 <= number of nodes <= 106
0 <= node -> data <= 105
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def solve(root, ans, l):
    if root is None:
        return ans
    
    if l == len(ans):
        ans.append(root.data)
    solve(root.left, ans, l+1)
    solve(root.right, ans, l+1)

def leftView(root):
    ans = []
    solve(root, ans, 0)
    return ans

n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.right = Node(3)
n.left.right = Node(5)
print(leftView(n))