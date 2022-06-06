from cgitb import text
from tkinter import *

import speedtest as s

def speedcheck():
    sp=s.Speedtest()
    sp.get_servers()
    down_1= sp.download()/(10**6)
    down = str(round(down_1,3))+"Mbps"
    upl_1= sp.upload()/(10**6)
    upl = str(round(upl_1,3))+"Mbps"
    dwn1.config(text=down)
    upl1.config(text=upl)
    


sp=Tk()
sp.title("INTERNET SPEED")
sp.geometry("500x600")
sp.config(bg="blue")
lab=Label(sp,text="Internet Speed Test Below",font=("Time New Roman",20,"bold"),bg="blue",fg="Red")
lab.place(x=50,y=50,height=50,width=400)
dwn=Label(sp,text="Download speed",font=("Time New Roman",20,"bold"),bg="blue")
dwn.place(x=50,y=150,height=50,width=400)
dwn1=Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="blue",fg='White')
dwn1.place(x=50,y=250,height=50,width=400)
upl=Label(sp,text="Upload speed",font=("Time New Roman",20,"bold"),bg="blue")
upl.place(x=50,y=350,height=50,width=400)
upl1=Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="blue",fg='White')
upl1.place(x=50,y=450,height=50,width=400)
btn=Button(sp,text="Start",font=("Time New Roman",20,"bold"),relief=RAISED,bg="white",fg="Red",command=speedcheck)
btn.place(x=200,y=550,height=50,width=100)
sp.mainloop()