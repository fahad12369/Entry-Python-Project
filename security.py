"""
Security 
"""

known_users = ["Alice", "Bob", "Claire", "Emma", "Fred", "Georgie", "Harry"]

while True:
  print("Hi! My name is Travis")
  name = input("What is your name? ").strip().capitalize()

  if name in known_users:
    print("Hello {}".format(name))
    remove = input("Would you like to be removed from the system (y/n)?: ").lower().strip()
    if remove =="y":
      known_users.remove(name)
      
    elif remove == "n":
      print("I didn't want you to leave anyway!" )
  else:
    print("I don't think I have met you yet {}! ".format(name))
    add_me = input("Would you like to be added to the system (y/n)?: ").lower().strip()
    if add_me == "y":
      known_users.append(name)
    elif add_me == "n":
      print("No worries, have a great day! ")

