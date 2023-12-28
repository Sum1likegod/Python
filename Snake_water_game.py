import random 

while True:

  sn_wa_gu = [0,1,2]
  comp = random.choice(sn_wa_gu)
  user = int(input("Enter 0 for snake, 1 for water and 2 for gun: "))
  if user == 5:
    break
  if not -1 < int(user) < 3:
    raise ValueError("Invalid input")
  print(f'\t\tComputer\'s Input is {comp}')
  print(f'\t\tUser\'s Input is {user}')
  if comp == user:
    print("The Game Has Been Drawed")
  elif (comp == 0 and user == 2) or (comp == 1 and user == 0) or (comp == 2 and user == 1):
    print("User Won The Game")
  elif (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
    print("User Lose The Game")
