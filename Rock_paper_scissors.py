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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user ==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)
elif user>2:
    print("your input is invalid , try again\n program terminated")
    exit()
else:
    print("Something went wrong try again")



computer = random.randint(0,2)

print("Computer chose:")

if computer ==0:
    print(rock)
elif computer==1:
    print(paper)
elif computer==2:
    print(scissors)
else:
    print("Something went wrong try again")


if (user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1):
    print("you win")
elif user==computer:
    print("draw")
else:
    print("you lose")


