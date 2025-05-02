'''
Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.

Examples:

Input: mat[][] = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
Output: 1
Explanation: Oranges at positions (0,2), (1,2), (2,0) will rot oranges at (0,1), (1,1), (2,2) and (2,1) in unit time.
Input: mat[][] = [[2, 2, 0, 1]]
Output: -1
Explanation: Oranges at (0,0) and (0,1) can't rot orange at (0,3).
Input: mat[][] = [[2, 2, 2], [0, 2, 0]]
Output: 0
Explanation: There is no fresh orange. 
Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[0].size() ≤ 500
mat[i][j] = {0, 1, 2} 
'''

from collections import deque
def rottenOranges(arr):
    n = len(arr)
    m = len(arr[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append([i, j, 0])
                visited[i][j] = 1
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    tm = 0
    while q:
        val = q.popleft()
        tm = max(tm, val[2])
        for i in range(4):
            r = dr[i] + val[0]
            c = dc[i] + val[1]
            if r >= 0 and r < n and c >= 0 and c < m and arr[r][c] == 1 and not visited[r][c]:
                q.append([r, c, tm+1])
                arr[r][c] = 2
                visited[r][c] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return -1
    return tm   

arr = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
print(rottenOranges(arr))