#functions go here
#yes no functions input for yes/no answer
def yes_no(question):
  valid = False
  while not valid:
    # asks user for input
    response = input(question).lower().strip()
    if response == "yes" or response == "y":
      response = "yes"
      return response
    elif response == "no" or response == "n":
      response = "no"
      return response
    else:
      print("Please enter yes or no")
      
#function to display instructions
def instructions():
  print("*** How to play with ***\n")
  print(""" Welcome to lucky unicorn, the cost is $1 per round to play. 
  If you get a unicorn you win $5. 
  If your recieve a Horse or Zebra you win 50c. 
  A donkey gets you nothing. Good luck!\n""")

#assess number is valid and within range
def int_check(question):
  error = "Please enter a whole number between 1 and 10"
  valid = False
  while not valid:
    try:
      response = int(input(question))

      if response < 1 or response > 10:
        print("Error: Number out of range")
      # output an error
      else:
        return response
  
    except ValueError:
      print(error)
  


# main program 
# loop for testing 
valid = False
while not valid:
  show_instructions = yes_no("Have you played before? ")
  if show_instructions =="no":
    print (instructions())

  how_much = int_check("How much would you like to play with? ")
  print("You have chosen to play with ${:.2f}".format(how_much))
