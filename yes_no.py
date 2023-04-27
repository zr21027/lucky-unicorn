#loop for testing
valid = False
while not valid:
  played_before = input("Have you played before?").lower()

  if played_before == "yes":
    print("Program continues")
  elif played_before == "y":
    print("Program continues")
  elif played_before == "no":
    print("Display insturctions")
  elif played_before == "n":
    print("Display instructions")
  else:
    print("Please enter yes or no")
