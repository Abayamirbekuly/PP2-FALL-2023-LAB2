'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
if x < y:
    print(x)
else:
    print(y)
