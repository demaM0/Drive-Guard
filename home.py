#Import the required Libraries
from tkinter import *
from tkinter import ttk
import time
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("750x270")

def open_popup_DRIVER():
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("DRIVER ON THE ROAD")
   top.resizable(False, False)
   # Create Entry Widgets for HH MM SS
   sec = StringVar()
   Entry(top, textvariable=sec, width=2, font='Helvetica 14').place(x=220, y=120)
   sec.set('00')
   mins = StringVar()
   Entry(top, textvariable=mins, width=2, font='Helvetica 14').place(x=180, y=120)
   mins.set('00')
   hrs = StringVar()
   Entry(top, textvariable=hrs, width=2, font='Helvetica 14').place(x=142, y=120)
   hrs.set('00')
   # Define the function for the timer

   def countdowntimer():
      times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
      while times > -1:
         minute, second = (times // 60, times % 60)
         hour = 0
         if minute > 60:
            hour, minute = (minute // 60, minute % 60)
         sec.set(second)
         mins.set(minute)
         hrs.set(hour)
         # Update the time
         top.update()
         time.sleep(1)
         if (times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
         times -= 1

   Label(top, font=('Helvetica bold', 22), text='Set the Timer').place(x=105, y=70)
   Button(top, text='START', bd='2', bg='IndianRed1', font=('Helvetica bold',10), command = countdowntimer).place(x=167, y=165)
def open_popup_REPORT():
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("Reports")

Label(win, text="choose the mode", font=('Helvetica 14 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(win, text= "Driving", command= open_popup_DRIVER).pack()
#ttk.Button(win, text= "Reports", command= open_popup_REPORT).pack()
win.mainloop()