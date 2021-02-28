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
choice = [rock, paper, scissors] #Adding to list
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number. You lose.")
else:
    print(choice[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: \n" + choice[computer_choice])

    if computer_choice == 2 and user_choice == 0:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice < user_choice:
        print("You win")
    else:
        print("You draw")