print('                  WELCOME TO THE RESULT PORTAL            ')

tot_mar=input('Enter Total Marks: ')
mar_obt=input('Enter marks obtained: ')
percent=(float(mar_obt)/float(tot_mar)*100)

print('Your Percentage is: ',percent)
if(percent>33.0):
    print('Whola! You Cracked the examination')
else:
    print("Better luck next time. You didn't make it)
    	
