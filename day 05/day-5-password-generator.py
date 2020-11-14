#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Betsy's Password Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letterchoice = ''
symbolchoice = ''
numberchoice = ''

for l in range(nr_letters):
  letterchoice+=random.choice(letters)

for s in range(nr_symbols):
  symbolchoice+=random.choice(symbols)

for n in range(nr_numbers):
  numberchoice+=random.choice(numbers)
  
password_total = letterchoice + symbolchoice + numberchoice

i = list(password_total)
random.shuffle(i)
password = ''.join(i)

print(f"Your password is: {password} ")







