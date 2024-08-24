import guessNum_art
import random

rand_num = random.randint(1,100)
def compare(guess, num): 
  if guess < num:
    print("Too low.")
    print("Guess again.")
  elif guess > num:
    print("Too high.")
    print("Guess again.")
  elif guess == num:
    print(f"You make it. the num is {num} ")

  return guess == num
    
  
  

print(guessNum_art.logo)



#test
#print(f"rand_num = {rand_num}")

print("Welcome to the Number Guessing Game!")
print("I'm thingking of a number between 1 and 100.")

diffi_level = input("Choose a difficulty. Tpye 'easy' or 'hard'：")

if diffi_level == "easy":
  total_guess_time = 10
else:
  total_guess_time = 5

left_guess_time = total_guess_time

while left_guess_time > 0:
  print(f"You have {left_guess_time} attempts remaining to guess the number. ")
  user_guess = int(input("Make a guess: "))
  if compare(user_guess,rand_num):
    break
  left_guess_time -= 1 
  if left_guess_time == 0:
    print(f"You run out of chances. The num is {rand_num}")
