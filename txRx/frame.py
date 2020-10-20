
# var = StringVar()
# label = Label(labelframe1, textvariable=var)
# var.set("Hey!? How are you doing?")
# label.config(height=0, width=20)
# label.pack()

from Tkinter import *

window =Tk()
window.title('GUI SERVER')
window.geometry('600x500')

#title1

subFramel =Frame(window, bg='#F8F8F8', width=300,height=500).place(x=0,y=0)

title1 = Label(window, text='SERVER',font=("Helvetica",35)).place(x=50,y=0)
label = Label(window, text="Data diserver = "+"1000",font=(30))
label.place(x=50,y=200)
labe2 = Label(window, text="remainder decode server = "+"10000",font=(30))
labe2.place(x=50,y=220)
    

#title2
subFrame2 =Frame(window, bg='#A9A9A9',width=300,height=500).pack(side='right')

title1 = Label(window, text='SENDER',font=("Helvetica",35)).place(x=350,y=0)
title1 = Label(window, text='SERVER',font=("Helvetica",35)).place(x=50,y=0)
label = Label(window, text="Data diserver = "+"1000",font=(30))
label.place(x=350,y=200)
labe2 = Label(window, text="remainder decode server = "+"10000",font=(30))
labe2.place(x=350,y=220)
window.mainloop()