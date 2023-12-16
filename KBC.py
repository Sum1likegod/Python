def ques_print(ques):
  for i in range(0,len(ques)):
    print (ques[i])  
  

money=0
exit=3
ques1 =   ["The International Literacy Day is observed on",
"\t\tA. Sep 8",
"\t\tB. Nov 28",
"\t\tC. May 2",
"\t\tD. Sep 22"]


ques_print(ques1)

ans1 = input("Enter your answer: ")

if ans1 == ques1[1] or ans1 == 'A' or ans1 == 'a':
  print('Correct answer')
  money+=1000
else:
  print('\tWrong Answer\nLets try next question')
  exit-=1



ques2=['The language of Lakshadweep. a Union Territory of India, is',
      '\t\tA. Tamil',
      '\t\tB. Hindi',
      '\t\tC. Malayalam',
      '\t\tD. Telugu'    ]  

ques_print(ques2)

ans2 = input("Enter your answer: ")

if ans2 == ques2[2] or ans2 == 'C' or ans2 == 'c':
  print('Correct answer')
  if exit == 3:
    money+=5000
  else:
    money+=1000
else:
  print('\tWrong Answer\nLets try next question')
  exit-=1


ques3=['In which group of places the Kumbha Mela is held every twelve years?',
      '\t\tA. Ujjain. Purl; Prayag. Haridwar',
      '\t\tB. Prayag. Haridwar, Ujjain,. Nasik',
      '\t\tC. Rameshwaram. Purl, Badrinath. Dwarika',
      '\t\tD. Chittakoot, Ujjain, Prayag,Haridwar']

ques_print(ques3)

ans3 = input("Enter your answer: ")

if ans3 == ques3[2] or ans3 == 'B' or ans3 == 'b' :
  print('Correct answer')
  if exit == 3:
    money+=10000
  elif exit == 2:
    money+=5000
  else:
    money+=1000
else:
  print('\tWrong Answer\nLets try next question')
  exit-=1



print('Thank You for Playing KBC\n You have won',money,'rupees')

     