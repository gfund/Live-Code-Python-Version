import traceback
import subprocess
import time
import sys
#Continually be running the code 
global past_version
past_version="" #keep past version of code read

def detect_delta():
  global past_version
  while True:
   
    file=open("script.py","r")
    file_contents=file.read()
    past_version_holder=past_version #create a var with past versions data so it can be replaced with what was read without interfering with the comparison
    past_version=file_contents
  
    if((past_version_holder!=file_contents) ):
     clean_terminal()
    return (past_version_holder!=file_contents) #check if the past version of the script is the same as the file contents,compare with holder so past version can be overwritten
  
def clean_terminal():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
def run_code():
   
   
     x=subprocess.Popen(f"{sys.executable} script.py",shell=True)
   
     time.sleep(10)
     x.terminate()
    
    
    
      
   
while True:
  if(detect_delta()):
   try:#catch exceptions
    
   
    run_code()

  
    
    

      
   except Exception:
  #Print stack trace for the user to see 
    traceback.print_exc()


