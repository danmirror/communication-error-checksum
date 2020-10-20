  #!/usr/bin/env python
   
import Tkinter as tk
import time
   
top = tk.Tk()
   
def addText():
    # make first change
    oldText = L.cget("text")
    newText = oldText + '\nfirst change'
    L.configure(text=newText)
   
    # wait 2 seconds
    top.update_idletasks()
    time.sleep(2)
   
    # make second change
    newText += '\nsecond change'
    L.configure(text=newText)
   
B = tk.Button(top, text ="Change text", command = addText)
L = tk.Label(top,text='orignal text')
   
B.pack()
L.pack()
top.mainloop()