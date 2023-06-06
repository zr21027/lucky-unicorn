import random 

# functions go here
def yes_no (question):
  valid = False
  while not valid:
    response = input(question).lower().strip()

    if response == "yes" or response == "y":
        response = "yes"
        return response
  
    elif response == "no" or response == "n":
      response = "no"
      return response
  
    else:
      print("Please enter yes or no")

def num_check(question):
    error = "Please enter an whole number between 1 and 10\n"
    
    valid = False
    while not valid:
      try:
# ask the question
        response = int(input(question))
#if the amount is too low/ too high give
        if response < 1 or response > 10:
          print("Error: Number out of range")
# output an error
        else:
          print("You have chosen to play with {}".format(response))
          return response
    
      except ValueError:
        print(error)
    
# main routine   
valid = False
while not valid:
  show_instructions = yes_no("Have you played before? ")
  if show_instructions =="no":
    print ("display instructions")
  #ask user how uch to play with
  how_much = num_check("How much would you like to play with? ")
  print()
  
  balance = how_much
  # set up play loop to engage game and play multiple rounds
  play_again = input("Please press <enter> to play ...")
  while play_again == "":
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

    #if out of money game will end
    if balance <1:
      play_again = "xxx"
      print("Sorry you have run out of money")
    # option to play again or exit game after round
    else:
      play_again = input("Do you want to play again? press <enter>")
  
  