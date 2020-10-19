#%%
"19/10/2020"

#  Digital time with python
import sys
from  tkinter import *
import time 

def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time)
	clock.after(100,times)  # times and delay


root=Tk()
root.geometry("150x120")    # frame size 
clock=Label(root,font=("times",20,"bold"),bg="lightblue")   # times shapes and color
clock.grid(row=2,column=2,pady=8,padx=30)
times()

#labels
digi=Label(root,text="Digital clock",font="times 15 bold")
digi.grid(row=1,column=2)  #times labell Title where and shapes
#
nota=Label(root,text="Hour   Minute   Second   ",font="times 10 bold")
nota.grid(row=3,column=2)        #defination labell Title where and shapes

root.mainloop()


