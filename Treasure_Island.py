print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right'\n").lower()
if first_choice == 'left':
    second_choice = input("You've come to a lake. There is an island in the middle of the lake.\n   Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_choice == 'wait':
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if third_choice == 'red':
            print("Burned by fire.Game Over.")
        elif third_choice == 'blue':
            print("Eaten by beasts.Game Over.")
        elif third_choice == 'yellow':
            print("You Win!")
        else:
            print("Game over")

    elif second_choice == 'swim':
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("something went wrong try again")

elif first_choice== 'right':
    print("You fell into a hole. Game Over.")
else:
    print("something went wrong try again")


