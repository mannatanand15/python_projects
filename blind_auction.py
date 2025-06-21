# TODO-1: Ask the user for input
import art
print(art.logo)

def highest_bid(bidding_dictionary):
    winner=""  #empty string to get key
    highest_bid=0  #variable whose values changes in every loop
    for bidder in bidding_dictionary:     #loop through keys not values
        bid_amount=bidding_dictionary[bidder]     #define key and tap into key to get values
    if bid_amount>highest_bid:
        highest_bid=bid_amount
        winner=bidder
    print(f"the winner is {winner} with bid $ {bid_amount}")
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
bid ={}
new=True
while new:
    name=input("what is ur name?\n")
    price=int(input("What is your bid?$\n"))
    bid[name]=price
    new=input("are there any more bidders?type 'yes' or 'no'.\n").lower()
    if new=='no':
        new=False
        highest_bid(bid)
    elif new =="yes":
        print("\n"*100)


# TODO-4: Compare bids in dictionary



