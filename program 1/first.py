# write a program to check if a number entered by the user is odd or even


num = int(input("enter a number: "))

rem = num % 2

if (rem == 0):
    print("EVEN")
else:
    print("ODD")
    