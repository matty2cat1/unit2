#Matt Westelman
#warmup3.py - get the brain working
#1/31/18

num = int(input("Pick a number"))
if num%2==0 and num%3==0:
    print(num, "is divisible by both 2 and 3")
elif num%2==0 and num%3!=0:
    print(num, "is divisible by 2 but not 3")
elif num%2!=0 and num%3==0:
    print(num, "is divisible by 3 but not 2")
else:
  print(num, "is not divisible by 2 nor 3")
