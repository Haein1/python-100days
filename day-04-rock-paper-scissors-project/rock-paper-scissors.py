import random
rock = '''
    _______
000---'   ____)
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

choices = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choices[user_choice])

computer_choice = random.randint(0,2)
print("computer chose:")
print(choices[computer_choice])

final_res = ""
win = "You win!"
lose = "You lose!"
draw = "It's a draw!"
if user_choice == 0:#user : rock
    if computer_choice == 2:
        final_res = win
    elif computer_choice == 0:
        final_res = draw
    else:
        final_res = lose
elif user_choice == 1:#user : paper
    if computer_choice == 0:
        final_res = win
    elif computer_choice == 1:
        final_res = draw
    else:
        final_res = lose
elif user_choice == 2:#user : scissors
    if computer_choice == 1:
        final_res = win
    elif computer_choice == 2:
        final_res = draw
    else:
        final_res = lose

print(final_res)
