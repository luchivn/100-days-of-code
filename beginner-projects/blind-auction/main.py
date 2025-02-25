from art import logo as logo

print(logo)

answer = "yes"
dictionary = {}

while answer == "yes":
    bidder = input("Enter your name: ")
    price = float(input("Enter your price: $"))

    dictionary[bidder] = price

    answer = input("Are there more bidders? Type 'yes' or 'no'.\n")

    print("\n"*10)

maximum = 0
name = ""

for bidder in dictionary:
    if dictionary[bidder] > maximum:
        maximum = dictionary[bidder]
        name = bidder

print("The winner is " + name + " with a bid of $" + str(maximum))
