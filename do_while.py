age = int(input('Enter The Candidate\'s Age '))
while (age > 0):
  if age < 18:
    print('The Candidate is Underage')
    break
  elif age > 110:
    print('The Candidate is Dead\n\t!!!Enter Valid Age!!!')
  elif age > 18:
    print('You\'re Eligble For Vote' )
  age = int(input('Enter The Candidate\'s Age '))
