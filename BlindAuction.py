import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders_flag = True
bidders = []
print(logo)

def clear():
    if os.name == 'nt':
      os.system('cls')
    else:
       os.system('clear')

def ask_more_bids(flag=True):
  while flag:
    more_bids = input("\nAre there any other bidders? Type 'yes' or 'no'.\n")
    if more_bids == 'yes':
        clear()
        flag = False
        return "yes"
    elif more_bids == 'no':
        flag = False
        return "no"
    else:
        print("Invalid option.")

while bidders_flag:

  new_bid = {}
  name = input("What is your name?: ")
  bid = float(input("What is your bid?: $"))
  new_bid[name] = bid
  bidders.append(new_bid)
  ask_bid = ask_more_bids()

  if ask_bid == 'yes':
      continue
  else:
    winner_name = ''
    winner_bid = 0
    for dictionary in bidders:
        for key in dictionary:
            if winner_bid < dictionary[key]:
               winner_bid = dictionary[key]
               winner_name = key
    
    print(f"\nThe winner is {winner_name} with a bid of ${winner_bid:.2f}")
    bidders_flag = False
