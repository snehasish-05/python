import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_cards_1 = []
total = 0
total1 = 0



while True:
    print(logo)
    play = input("Do you want to play a game of Blackjack? Type 'y' 'or' 'n' ").lower()
    if play == 'y':
        user = random.choices(cards,k=2)
        computer = random.choices(cards,k=2)
        computer_cards.extend(computer)
        user_cards.extend(user)
        total = sum(user_cards)
        total1 = sum(computer_cards)
        print(f"Your cards: {user_cards}, current score: {total}")
        print(f"Computer's first card: {computer_cards[0]}")
        con = input("Do you want to pick another card: 'y' 'or' 'n' ").lower()
        if con == 'y':
            user1 = random.choice(cards)
            user_cards.append(user1)
            com1 = random.choice(cards)
            computer_cards.append(com1)
            tot = sum(user_cards)
            tot1 = sum(computer_cards)
            total = tot
            total1 = tot1

            user_cards_1 = user_cards
            break
        else:
            break



    else:
        exit()

print(f"Your final cards: {user_cards}, final score: {total} ")
print(f"Computer final: {computer_cards}, final score: {total1} ")

if total>21 and total1>21:
    print("It is a Draw")
elif total>21 and total1<=21:
    print("You lose because you went over 21")
elif total<=21 and total1>21:
    print("You win")
elif total<=21 and total1<=21:
    if total == total1:
        print("Draw")
    elif total>total1:
        print("you_win")
    elif total<total1:
        print("you_lose")



