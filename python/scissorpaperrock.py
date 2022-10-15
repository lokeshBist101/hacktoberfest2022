import random
print("Welcome to ROCK SCISSORS PAPER")


rock='''
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

game_images=[rock,paper,scissors]
your_choice=int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for scissors "))
print(game_images[your_choice])

computer_choice=random.randint(0,2)

print(f"Computer chose:")

print(game_images[computer_choice])

if computer_choice== 2 and your_choice==0:
  print("You Win!!")

elif computer_choice==0 and your_choice==2:
  print("You lose!!")

elif computer_choice>your_choice:
  print("You lose!")

elif your_choice>computer_choice:
  print("You win!!")

elif computer_choice==your_choice:
  print("Tie!!")