rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

import random

options = [rock,paper,scissors]

length_options = len(options)

random_option = random.randint(0,length_options-1)

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))


if input == random_option:
    print("You choose: \n", options[input])
    print("Computer choose: \n", options[random_option])
    print("It's draw")

elif input == 2 and random_option == 0:
    print("You choose: \n", options[input])
    print("Computer choose: \n", options[random_option])
    print("You lose!")

elif input > random_option:
    print("You choose: \n", options[input])
    print("Computer choose: \n", options[random_option])
    print("You win!")

elif input < random_option == 'rock':
    print("You choose: \n", options[input])
    print("Computer choose: \n", options[random_option])
    print("You lose!")

elif input == 0 and random_option == 2:
    print("You choose: \n", options[input])
    print("Computer choose: \n", options[random_option])
    print("You win!")


