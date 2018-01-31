#Matt Westelman
#fortuneTeller - What is your fortune
#1/30/18

color = input("red or blue? ")
num = int(input("pick a number between 1 and 4 "))
if color == "blue" and num == 1:
    print("Today isn't your lucky day")
elif color == "blue" and num == 2:
    print("Today might be your lucky day")
elif color == "blue" and num == 3:
    print("I would stay away from fire if I were you...")
elif color == "blue" and num == 4:
    print("I see lots of coding in your future")
elif num == 1:
    print("I hope you like spaghetti")
elif num == 2:
    print("You have to wake up")
elif num == 3:
    print("Dinner will be ready soon")
elif num == 4:
    print("Look behind you...")
