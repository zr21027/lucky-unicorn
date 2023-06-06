import random 

# main routine goes here
tokens = ["unicorn",  "horse", "horse", "horse" 
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"]
starting_balance = 100

balance = starting_balance
# testing loop to generate 20 tokens
for item in range (0,20):
  chosen_num = random.randint(1, 100)

  # adjust balance
  if chosen == "unicorn":
      balance += 4
  elif chosen == "donkey":
      balance -= 1
  else:
      balance -= 0.5


print ()
print("Starting balance: ${:.2f}".format(starting_balance))
print("Final balance: ${}".format(balance))
