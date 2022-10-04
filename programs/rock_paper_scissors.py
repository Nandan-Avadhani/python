# rock paper scissors
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
choices = [rock,paper,scissors]
choice = int(input("enter your choice 0 for rock 1 for paper 2 for scissors"))
if choice > 2 or choice < 0:
    print("invalid choice game over")
else:
    print(choices[choice])
    system = random.randint(0,2)
    print(f"system chose {system}\n{choices[system]}")
    
    if choice == system:
        print("its a draw")
    elif choice == 0 and system == 1:
        print("you lose")
    elif choice == 0 and system == 2:
        print("you win")
    elif choice == 1 and system == 0:
        print("you win")
    elif choice == 1 and system == 2:
        print("you lose")
    elif choice == 2 and system == 0:
        print("you lose")
    elif choice == 2 and system == 1:
        print("you win")
        


