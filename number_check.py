#functions go here
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
# loop for testing 
valid = False
while not valid: 

  how_much = num_check("How much would you like to play with? ")
  print()

