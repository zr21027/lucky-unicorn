import random 

# main routine goes here

starting_balance = 100

balance = starting_balance
# testing loop to generate 20 tokens
for item in range (0, 10):
  chosen_num = random.randint(1, 100)

  # adjust balance
  if 1 <= chosen_num <= 5: 
      chosen = "unicorn"
      balance += 4
  elif 6 <= chosen_num <= 36:
      chosen = "donkey"
      balance -= 1
  else:
      if chosen_num % 2 == 0:
        chosen = "horse"
      else:
        chosen = "zebra"
      balance -= 0.5

  print("You got a {}. Your balance is ""${:.2f}".format (chosen, balance))
  
  print()

# set up play loop to engage game and play multiple rounds
play_again = input("Please press <enter> to play ...")
while play_again == "":

  #token selection goes here from component

  #if out of money game will end
  if balance <=1:
    play_again = "xxx"
    print("Sorry you have run out of money")
  # option to play again or exit game after round
  else:
    play_again = input("Do you want to play again? press <enter>")