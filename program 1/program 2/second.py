# write a program to find the greatest of three numbers entered by the user

65
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >=b and a >= c):
    print("first number is largest",a)

elif(b >= c):
    print("second number is largest",b)
