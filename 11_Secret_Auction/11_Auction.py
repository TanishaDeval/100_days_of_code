import gavel_art
print(gavel_art.gavel)
print("*  *  *  Welcome to Secret Auction  *  *  * \n")

def finding_highest_bidder(bidders):
    highest_bid=0
    winner=""
    for name in bidders:
        if bidders[name]>highest_bid:
            highest_bid=bidders[name]
            winner=name
    print(f"🎉 Winner is {winner} with highest bidding of ₹{highest_bid}" )
auction_running=True
bidders = {}
while auction_running:
    name=input("Enter your name:\n")
    bid=int(input("Enter your bid:\n₹"))
    bidders[name]=bid

    any_other_bidder=input("Is there any other bidder (yes / no ):\n").lower()
    if any_other_bidder=="yes":
       print("\n "* 100)
    else:
        auction_running = False
        finding_highest_bidder(bidders)












