#Matt Westelman
#brogue
#2/2/18

print("You open the door, and see an axe and a rapier")
weapon = input("Which do you pick up? (axe or rapier)")
if weapon == "axe":
    axeEquip = input("equip the axe? (yes or no)")
    if axeEquip == "yes":
        print("You can barely lift its massive weight: 2 more strength would be ideal")
    else:
        ("you put the axe in your pack")
elif weapon == "rapier": 
    swordEquip = input("equip the rapier? (yes or no)")
    if swordEquip == "yes":
        print("Your grip involontarily tightens around the sword. It must've been cursed!")
    else:
        print("you put the rapier in your pack")
else: 
    print("You took to long to think! A kobold attacks you.")
