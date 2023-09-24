'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
m=int(input())
k=int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")
