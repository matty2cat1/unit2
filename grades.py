#Matt Westelman
#grades - if statements
#1/29/18

grade = int(input("What was your grade? "))
if grade >= 90:
    print("Hey, thats an A!")
elif grade >= 80 and grade < 90:
    print("Nice, that's a B")
elif grade >= 70 and grade < 80:
    print("That's a C")
elif grade >= 50 and grade < 60:
    print("Study harder, that's a D")
elif grade >= 0 and grade < 50:
    print("You should not have gotten out of bed today...")
