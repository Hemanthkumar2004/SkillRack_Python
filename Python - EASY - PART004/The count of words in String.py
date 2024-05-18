'''
The program must accept a string S and print the count of words in S.
Boundary Condition(s): 1 <= Length of S <= 1000
Input Format: The first line contains S.
Output Format: The first line contains the integer value representing the word count.
Example Input/Output 1:
Input: I like tea
Output: 3
Example Input/Output 2:
Input: I like coffee very much
Output: 5
'''
s=input().split()    
print(len(s))
