import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_imgs = [rock, paper, scissors]

print("Welcome to the Rock, Papers, and Scissors game!\n")

ask_user = int(input("Which one will you choose? Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS.\n"))
print(game_imgs[ask_user])

bot = random.randint(0,2)

print("Computer chose:\n")
print(game_imgs[bot])

if ask_user == bot:
  print("It's a tie!")
elif (ask_user > bot) or (ask_user == 0 and bot == 2):
  print("You Win!")
elif (ask_user < bot) or (ask_user == 2 and bot == 0):
  print("You Lose! Better luck next time.")
elif (ask_user == bot):
  print("It's a tie!")