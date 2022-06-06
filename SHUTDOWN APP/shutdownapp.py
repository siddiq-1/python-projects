import imp
from tkinter import *
import os
from click import command

from flask import Blueprint
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")
    

st=Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="Blue")
r_button=Button(st,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)
rt_button=Button(st,text="Restart-Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)
l_button=Button(st,text="Log out",font=("Time New Roman",15,"bold"),relief=RAISED,cursor="plus",command=log_out)
l_button.place(x=150,y=280,height=50,width=200)
s_button=Button(st,text="shutdown",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus",command=shutdown)
s_button.place(x=150,y=390,height=50,width=200)


st.mainloop()
 