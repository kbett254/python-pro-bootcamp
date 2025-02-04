import random

symbols = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
,

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
]

game_list = ['rock', 'paper', 'scissors']
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You chose {game_list[user_choice]}")
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

else:
    print(symbols[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {game_list[computer_choice]}")
    print(symbols[computer_choice])


    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
