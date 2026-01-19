import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

results = [rock, paper, scissors]

player_1_pick = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_pick = random.randint(0, 2)

print("\nYou choose: ")
print(results[int(player_1_pick)])

print("\n\n Computer chose: ")
print(results[computer_pick])



