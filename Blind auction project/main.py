from art import logo
other_bid = True
dict_ = {}
name = ""
bid = 0
print(logo)
while other_bid:
    name = input("What is your name\n").lower()
    bid = int(input("What is your bid $\n"))
    dict_[name]=bid
    other = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if other=='no':
        other_bid = False
    else:
        print("\n"*100)


winner_bid = max(dict_.values())
winner_name = ""


for key,value in dict_.items():
    if value == winner_bid:
        winner_name = key

print(f"The winner is {winner_name} with a bid of ${winner_bid}")













