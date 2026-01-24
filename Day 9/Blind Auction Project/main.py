from art import logo

print(logo)


people_to_bid = True
bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner


while people_to_bid:
    name = input("Please enter your name: \n")
    bid = int(input("Please enter your bid: \n"))
    bids[name] = bid

    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "no":
        people_to_bid = False

print(bids)

max_bid = max(bids.values())
winner = [name for name, bid in bids.items() if bid == max_bid]
print(f"The winner is {winner[0]} with a bid of ${max_bid}.")
