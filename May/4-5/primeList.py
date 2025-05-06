'''
You are given the head of a linked list. You have to replace all the values of the nodes with the nearest prime number. If more than one prime number exists at an equal distance, choose the smallest one. Return the head of the modified linked list.

Examples :

Input: head = 2 → 6 → 10
Output: 2 → 5 → 11

Explanation: The nearest prime of 2 is 2 itself. The nearest primes of 6 are 5 and 7, since 5 is smaller so, 5 will be chosen. The nearest prime of 10 is 11.
Input: head = 1 → 15 → 20
Output: 2 → 13 → 19

Explanation: The nearest prime of 1 is 2. The nearest primes of 15 are 13 and 17, since 13 is smaller so, 13 will be chosen. The nearest prime of 20 is 19.
Constraints:
1 <= no. of Nodes <= 104
1 <= node.val <= 104
'''

class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

def isPrime(val):
        if val == 1 or val == 2:
            return val
        mid = val//2
        for i in range(2,mid+1):
            if val%i == 0:
                return False
        return True
    
def nearestPrime(val):
        i =0
        f = False
        while not f:
            greater = isPrime(val+i)
            lower = isPrime(val-i)
            if lower:
                f = True
                return val-i
            if greater:
                f = True
                return val+i
            i += 1
    
def primeList(head):
        # code here
        tmp = head
        arr = []
        
        while tmp:
           arr.append(tmp.val)
           tmp = tmp.next
        
        res = None
        tmp = res
        for i in range(len(arr)):
            num = nearestPrime(arr[i])
            newNode = Node(num)
            if tmp is None:
                res = newNode
                tmp = res
            else:
                while tmp.next:
                     tmp = tmp.next
                tmp.next = newNode
                tmp = tmp.next
        printList(res)
        return res

def printList(head):
     tmp = head
     while tmp:
          print(tmp.val)
          tmp = tmp.next


n = Node(3)
n.next = Node(4)
n.next.next = Node(7)
n.next.next.next = Node(7)
print(primeList(n))