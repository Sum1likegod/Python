EX='This is the showcase for how enumerate function in python works'
for its_counting,letters in enumerate(EX):
  print(its_counting,letters,end=' ')


# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)


# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)