#Matt Westelman
#ifQuiz.py - A quiz on if statements
#2/12/18

word1 = input("Please enter a word! ")
word2 = input("Please enter another word! ")
if len(word1) > len(word2):
    print("Word 1 is longer")
elif len(word2) > len(word1):
     print("Word 2 is longer")
else:
     print("Your words are the same length!")

if "p" or "P" in word1 and "p" and "P" not in word2:
    print("Only the first word has a 'p'")
elif "p" or "P" in word2 and "p" and "P" not in word1:
    print("Only the second word has a 'p'")
elif "p" or "P" in word2 and "p" and "P" not in word1:
    print("Neither words have a 'p'")
else:
    print("Both words have a 'P'")

num1= int(input("Now enter a number"))
num2 = int(input("Please enter another number that will make the sum of the 2 numbers =12"))
if num1+num2==12:
    print("correct")
else:
    print("incorrect")
