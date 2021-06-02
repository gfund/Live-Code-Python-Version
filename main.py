import os.path
import traceback


while True:
 try:

   #read script lines
   
   

  #These lines will read the script 
  scriptfileread = open("script.py", "r")
  scriptlines=scriptfileread.read()
  #These lines will read 
  scriptfilewrite=open("script.txt","w+")
  scriptfilewrite.write(scriptlines)
  #Read the whats stored in the text file to compare with the script lines 
  textversionofscriptfile=open("script.txt","r")
  textlines=textversionofscriptfile.read()
  if scriptlines!=textlines:
   
   #Clean the terminal
   print(chr(27) + "[2J")
   #This line will run the script
   exec(open("script.py").read())
  else: 
    continue
 

    
 except Exception:
  traceback.print_exc()



