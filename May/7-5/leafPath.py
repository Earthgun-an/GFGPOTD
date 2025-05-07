'''
Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree.

Examples:

Input: root[] = [1, 2, 3, 4, 5, N, N]
ex-3
Output: [[1, 2, 4], [1, 2, 5], [1, 3]]
Explanation: All the possible paths from root node to leaf nodes are: 1 -> 2 -> 4, 1 -> 2 -> 5 and 1 -> 3
Input: root[] = [1, 2, 3]

Output: [[1, 2], [1, 3]] 
Explanation: All the possible paths from root node to leaf nodes are: 1 -> 2 and 1 -> 3
Input: root[] = [10, 20, 30, 40, 60, N, N]

Output: [[10, 20, 40], [10, 20, 60], [10, 30]]
Explanation: All the possible paths from root node to leaf nodes are: 10 -> 20 -> 40, 10 -> 20 -> 60 and 10 -> 30
Constraints:
1 <= number of nodes <= 104
1 <= node->data <= 104
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def solve(root, ans, tmp):
    if root is None:
        return
    
    tmp.append(root.data)
    if not root.left and not root.right:
        ans.append(tmp[:])
    else:
        solve(root.left, ans, tmp)
        solve(root.right, ans, tmp)
    tmp.pop()


def leafPath(root):
    ans = []
    solve(root, ans, [])
    return ans

n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.right = Node(3)
n.left.right = Node(5)
print(leafPath(n))