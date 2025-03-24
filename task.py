import random

# ASCII art
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

game_images = [rock, paper, scissors]
global computers_choice
# users choice
input_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if input_choice >= 0 and input_choice <= 2:
    print(game_images[input_choice])
    computers_choice = random.randint(0,2) # random choice
    print(f"Computer chooses:\n{game_images[computers_choice]}")

# game logic
if input_choice < 0 or input_choice > 2:
    print("You have typed an invalid number. You lose!")
elif input_choice == 0 and computers_choice == 2:
    print("You Win!")
elif input_choice == 2 and computers_choice == 0:
    print("You Lose")
elif input_choice > computers_choice:
    print("You Win!")
elif input_choice < computers_choice:
    print("You Lose")
else:
    print("It's Draw")
