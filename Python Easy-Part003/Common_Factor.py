'''
Given a set of numbers where all other numbers are multiple of the smallest number,
the program must find the count of the common factors C excluding 1.
Input Format: First line will contain the integer value N representing how many numbers are passed as input.
Next N lines will have the numbers. Output Format: First line will contain the count of common factors C.
Constraints: N will be from 2 to 20.

Sample Input/Output: Example 1: Input: 2 100 75

Output: 2

Explanation: The common factors excluding 1 are 5,25. Hence output is 2

Example 2: Input: 3 10 20 30

Output: 3

Explanation: The common factors excluding 1 are 2,5,10. Hence output is 3.

'''



n=int(input())
arr=[]
count=0
for i in range(n):
    arr.append(int(input()))
small=min(arr)
for j in range(2,small+1):
    c=0
    for a in range(n):
        if arr[a]%j==0:
            c=c+1
        else:
            continue
    if c==n:
        count=count+1
            
print(count)


