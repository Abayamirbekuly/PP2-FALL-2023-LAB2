'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x=int(input())
if((x%4==0) and (x%100>0) or (x%400==0)):
    print("YES")
else:
    print("NO")
