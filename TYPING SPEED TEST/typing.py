from time import *
import random as r

def mistake(text1,userinp):
    error=0
    for i in range(len(text1)):
        try:
            if text1[i]!=userinp[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed(time_1,time_2,userinp):               
    time_delay=time_2-time_1
    time_r=round(time_delay)
    speed=len(userinp)/time_r
    return round(speed)


text=['''All python programs (on Shutdown/Restart) given in this article, are well-tested and executed. Therefore be sure to save all documents before executing any program given here.\n\n''','''Make sure to save and close all documents before executing any program given below. Because after executing these codes (programs), your system gets shutdown/restart and you can lost your unsaved documents.\n\n''','''To shutdown or restart your computer system (PC or laptop) using a python code, you have to first import the os library and then use os.system() in this way:\n\n''']

text1=r.choice(text)

print("\n\n\t\t*******Lets Do Typing*********\n\n")
print(text1)
time_1=time()
userinp=input("Enter: ")
time_2=time()

print("\n Speed: ",speed(time_1,time_2,userinp))
print("Error: ",mistake(text1,userinp))
