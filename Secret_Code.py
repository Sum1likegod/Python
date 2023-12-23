translator = input("Enter what do you want to do Encoding or Decoding: ")
if translator == "Decoding" or translator == "D":
  inp_str = input("Enter the encoded string: ")
  
  str_item = inp_str.split()
  
  encoded = ''
  encoded_string = ''
  for i in range(len(str_item)):
    if (len(str_item[i]) > 3):
      First_trim = str_item[i][3:]        #For removing the first 3 characters
      Second_trim = First_trim[:-3]       #For removing the last 3 characters
      Last_trim = list(Second_trim)       #For converting the string into list
      poped_char = Last_trim.pop(len(Second_trim)-1)    #For replacing the last character
      Last_trim.insert(0,poped_char)      #For inserting the last character at the start
      encoded = ''.join(Last_trim)        #For converting the list into string
      
    else:
      letter = list(str_item[i])
      letter.reverse()
      encoded = ''.join(letter)
  
    encoded_string = encoded_string + ' ' + encoded#For Getting the final encoded string
  print(encoded_string)

elif translator == "Encoding" or translator == "E":
  inp_str = input("Enter a string: ")

  str_item = inp_str.split()

  coded = ''
  coded_string = ''
  for i in range(len(str_item)):
    if (len(str_item[i]) > 3):
      letter = list(str_item[i])
      popped_letter = letter.pop(0)
      letter.append(popped_letter)
      letter.insert(0,'wer')
      letter.append('sdv')
      coded = ''.join(letter)
    else:
      letter = list(str_item[i])
      letter.reverse()
      coded = ''.join(letter)

    coded_string = coded_string + ' ' + coded
  print(coded_string)