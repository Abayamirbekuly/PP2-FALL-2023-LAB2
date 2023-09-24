'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx=abs(x1-x2)
dy=abs(y1-y2)

if dx==1 and dy==2 or dx==2 and dy==1 :
    print('YES')
else:
    print('NO')
