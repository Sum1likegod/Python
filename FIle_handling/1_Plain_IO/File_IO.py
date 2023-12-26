# file_hand = open('filee.txt','r')
# output = file_hand.read()
# print(output)
# file_hand.close()


# file_app = open('filee.txt','a')      #appending will add the text not remove it and
# re_inpu = file_app.write('I am a new line')   #reenter the text as many times as the 
# file_app.close()                        #python code is run



# file_wri = open('filee.txt','w')      #writing will remove the current text and add 
# writing = file_wri.write('This is definetly the new text')  #replace it with the 
# file_wri.close()                      #input text



# with open('filee.txt','r') as fu:       #This is context manager method for handling the 
#   print(fu.read())                      #file. It automatically closes the file.