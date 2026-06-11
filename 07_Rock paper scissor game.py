import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
options = [rock,paper,scissor]

player = int(input("Type 0 for rock , 1 for paper , 2 for scissor :\n"))
if player < 0 or player >=3:
    print("Invalid number .You lose!")
else:
    player_choice=options[player]
    print(player_choice)
    print()

    print("Computer :")
    computer_choice=random.choice(options)
    print(computer_choice)
    print()

    if  player_choice == computer_choice:
        print("It's a tie")
    elif player == 0 and computer_choice == paper:
        print("You lose!")
    elif player == 0 and computer_choice == scissor:
        print("You win!")
    elif player == 1 and computer_choice == rock:
        print("You win")
    elif player == 2 and computer_choice == paper:
        print("You win!")
    else:
        print("You lose!")
