#Matt Westelman
#compoundDemo - compound if statements
#1/30/18

num = int(input("enter a number: "))

if num > 0 and num%7 == 0:
    print(num, "Is positive and divisible by 7")
elif num > 0:
    print(num, "Is positive and not divisible by 7")
elif num < 0 and num%7 == 0:
    print(num, "Is negative and divisible by 7")
elif num < 0 and num%7 != 0:
     print(num, "Is negative and divisible by 7")
else:
    print(num, "is zero")
