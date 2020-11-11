
print("Welcome to the Love Calculator!\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinednames = name1 + name2
lowernames = combinednames.lower()

t = lowernames.count("t")
r = lowernames.count("r")
u = lowernames.count("u")
e = lowernames.count("e")
firstdigit = t + r + u + e

l = lowernames.count("l")
o = lowernames.count("o")
v = lowernames.count("v")
e = lowernames.count("e")
seconddigit = l + o + v + e

lovescore = int(str(firstdigit) + str(seconddigit))

if (lovescore < 10) or (lovescore > 90):
  print(f"Your score is {lovescore}, you go together like coke and mentos")
elif (lovescore >=40) and (lovescore <=50):
  print(f"Your score is {lovescore}, you're all right together")
else:
  print(f"Your score is {lovescore}")

