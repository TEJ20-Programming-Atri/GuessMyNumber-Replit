
from random import randint as rand

min_number = 1
max_number = 6

# function that makes sure input is valid
def valid_input(prompt:str):
  while True:
    try:
      res = int(input(prompt))
      if min_number <= res <= max_number :
        return res
      else:
        print("Value must be a integer between the specified range")
    except ValueError:
      print("Value must be a integer between the specified range")

random_number = rand(min_number, max_number)

answer = valid_input(f"Guess a number between {min_number} and {max_number}: ")

if answer == random_number:
    print(f"The correct number was {random_number}!")
    print("You guessed the number correctly!")
else:
    print(f"You guessed the number {answer}.")
    print(f"The correct number was {random_number}!")