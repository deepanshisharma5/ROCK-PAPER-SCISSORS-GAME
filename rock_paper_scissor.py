#project 
#rock paper scissors

import random

images = [
    '''
    ROCK
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
''',
    '''
    PAPER
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
''',
    '''
    SCISSORS
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''
]

your_choice = int(input("What would you like to choose?\nType 0 for rock, 1 for paper, and 2 for scissors.\nYour choice: "))

if your_choice < 0 or your_choice > 2:
    print("Invalid choice. Please choose between 0, 1, or 2.")
else:
    print(images[your_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(images[computer_choice])

    if your_choice == computer_choice:
        print("It's a draw.")
    elif (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")
