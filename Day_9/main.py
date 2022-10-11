import ASCII


def main():
    print(f"{ASCII.gavel}\nWelcome to the secret auction program!")

    auction_info = {}
    new_bidder = True

    while new_bidder:
        name = input("What is your name? ")
        bid = int(input("What is your bid? "))

        # Update map
        auction_info[name] = bid

        iteration = input("Are any other bidders? Press enter to proceed or type 'no/n' to start auction.\n").lower()
        if "n" in iteration:
            new_bidder = False
            print("Let’s get the auction results!")

    # Find max value and print name
    max_bid = 0
    winner = ""
    #1 for name, bid in auction_info.items():
    for name in auction_info:
        bid = auction_info[name]
        if bid > max_bid:
            winner = name
            max_bid = bid
        elif bid == max_bid:
            winner += " and " + name

    print(f"This auction win {winner}!")

if __name__ == '__main__':
    main()