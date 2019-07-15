#! python3
import webbrowser , sys , pyperclip

sys.argv  # gives command passed as list 

#check if command line is passed
if len(sys.argv) > 1 :
    #['mapit.py' , 'Rohini' , 'New' , 'Delhi'] -> Rohini New Delhi
    address = ' '.join(sys.argv[1:])  #Turns list to string excluding first cmd
else:
    address = pyperclip.paste()
    
print (address)
webbrowser.open('https://www.google.com/maps/place/' + address)
