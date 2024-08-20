from replit import clear
import secret_auction_art

def find_new_bidder(bidder_info_list,name,bid):
    new_bidder = {}
    new_bidder[name] = bid
    bidder_info_list.append(new_bidder)

def find_max(bidder_info_list):
    max_name = ""
    max_price = -1
    for bidder_dic in bidder_info_list:
          for name,price in bidder_dic.items():
              if price > max_price:
                  max_price = price
                  max_name = name
    print(f"The winner is {max_name} with a bid of ${max_price}.")

print(secret_auction_art.logo)

all_bid = []
print("Welcome to the secret auction program.")

has_other_bidder = "yes"
while has_other_bidder == "yes":
    
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    find_new_bidder(all_bid, name, bid)
    has_other_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    
    clear()
                          

find_max(all_bid)
