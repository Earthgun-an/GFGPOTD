'''
Given two numbers as strings s1 and s2. Calculate their Product.
Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Examples:

Input: s1 = "0033", s2 = "2"
Output: "66"
Explanation: 33 * 2 = 66
Input: s1 = "11", s2 = "23"
Output: "253"
Explanation: 11 * 23  = 253
Input: s1 = "123", s2 = "0"
Output: "0"
Explanation: Anything multiplied by 0 is equal to 0.

'''

def checkZero(s):
    while s[0] == '0':
        s = s[1:]
    return s

def multiplyStrings(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    neg = 0

    if s1[0] == '-':
        neg = not neg
        s1 = s1[1:]
    
    if s2[0] == '-':
        neg = not neg
        s2 = s2[1:]

    prod = [0 for _ in range(n1+n2)]

    for i in range(n2-1, -1, -1):
        dt1 = int(s2[i])
        carry = 0
        for j in range(n1-1, -1, -1):
            dt2 = int(s1[j])
            prod[i+j+1] += (dt1*dt2) +  carry
            carry = prod[i+j+1] // 10
            prod[i+j+1] = prod[i+j+1] % 10
        
        next_index = i
        while carry:
            prod[next_index] += carry
            carry = prod[next_index] // 10
            prod[next_index] = prod[next_index] % 10
            next_index -= 1
    
    res = ''.join(str(i) for i in prod)
    res = checkZero(res)
    if neg and res != '0':
        return '-'+res
    return res 

print(multiplyStrings('0033', '22'))