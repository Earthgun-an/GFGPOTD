'''
Given an array of integers arr[] where, every element appears thrice except for one which occurs once.
Find that element which occurs once.

Examples:

Input: arr[] = [1, 10, 1, 1]
Output: 10
Explanation: 10 occurs once in the array while the other element 1 occurs thrice.
Input: arr[] = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]
Output: 3
Explanation: All elements except 3 occurs thrice in the array.
'''

def findUnique(arr):
    mp = {}
    ans = []
    for i in arr:
        if i not in mp:
            mp[i] = 1
        else:
            mp[i] += 1
    for key,_ in mp.items():
        if mp[key] == 1:
            return ans.append(key)
    return ans