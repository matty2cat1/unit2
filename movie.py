#Matt Westelman
#movie Highest rating for me?
#1/29/18

grade = int(input("How old are you? "))
if grade >= 18:
    print("You can watch R rated movies")
elif grade >= 17 and grade < 13:
    print("You can watch PG-13")
elif  grade <= 13:
    print("You can watch PG")
