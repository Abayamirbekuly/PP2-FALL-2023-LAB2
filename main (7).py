'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x=int(input())
y=int(input())
z=int(input())
if(x==y==z):
    print("3")
elif(x==y or y==z or x==z):
    print("2")
else:
    print("0")
