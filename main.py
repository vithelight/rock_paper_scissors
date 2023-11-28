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

#Write your code below this line 👇
import random
signs = [0, 1, 2]
r = signs[0]
p = signs[1]
s = signs[2]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.choice(signs)
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

if computer_choice == 0:
  print('Computer chose:')
  print(rock)
elif computer_choice == 1:
  print('Computer chose:')
  print(paper)
else:
  print('Computer chose:')
  print(scissors)

if user_choice == computer_choice:
  print('Draw')
elif user_choice == r and computer_choice == s:
  print('You win')
elif user_choice == s and computer_choice == p:
  print('You win')
elif user_choice == p and computer_choice == r:
  print('You win')
else:
  print('You lose')
