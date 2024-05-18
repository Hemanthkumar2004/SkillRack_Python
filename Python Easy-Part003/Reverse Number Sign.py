'''An integer value N is passed as the input.
The program must reverse the sign of N and print -N as the output.
Input Format: The first line contains N.
Output Format: The first line contains -N. Boundary
Conditions: -999999 <= N <= 999999
Example Input/Output 1: Input: 125
Output: -125
Example Input/Output 2:
    Input: -346
    Output: 346
Example Input/Output 3:
    Input: 0
    Output: 0'''
n=int(input())
if n==0:
    print(n)
else:
    print(-1*n)
