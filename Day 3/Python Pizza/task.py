print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0
peperoni_cost = 0
extra_cheese_cost = 1

if size == "S":
    total += 15
    peperoni_cost = 2
elif size == "M":
    total += 20
    peperoni_cost = 3
elif size == "L":
    total += 25
    peperoni_cost = 4

if pepperoni == "Y":
    total += peperoni_cost

if extra_cheese == "Y":
    total += extra_cheese_cost

print(f"Your final bill is: ${total}.")
total = 0
peperoni_cost = 0
extra_cheese_cost = 1

if size == "S":
    total += 15
    peperoni_cost = 2
elif size == "M":
    total += 20
    peperoni_cost = 3
elif size == "L":
    total += 25
    peperoni_cost = 4

if pepperoni == "Y":
    total += peperoni_cost

if extra_cheese == "Y":
    total += extra_cheese_cost

print(f"Your final bill is: ${total}.")
