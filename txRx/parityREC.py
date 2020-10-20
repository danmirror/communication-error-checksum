import socket
from Tkinter import *

jumlah = 0

def tkint(data,metode,ascii,jumlah_send,jumlah):


    window = Tk()
    window.title('GUI SERVER')
    window.geometry('600x500')

    if (metode=="y"):
        metode = "parity genap"
    elif(metode=="n"):
        metode = "parity ganjil"
    if (jumlah_send == jumlah):
        komentar = "tidak ada error"
    else:
        komentar = " ada error"

    subFramel = Frame(window, bg='#F8F8F8', width=300,height=500).place(x=0,y=0)
    title1 = Label(window, text='SERVER',font=("Helvetica",35)).place(x=50,y=0)
    label = Label(window, text="Data yang di terima = \n"+data,font=(30))
    label.place(x=20,y=200)
    labe2 = Label(window, text="metode yang di gunakan = "+metode,font=(30))
    labe2.place(x=20,y=240)
    labe2 = Label(window, text="nilai parity  = "+jumlah,font=(30))
    labe2.place(x=20,y=260)
    labe2 = Label(window, text="hasil  = "+komentar,font=(30))
    labe2.place(x=20,y=280)

    #title2
    subFrame2 = Frame(window, bg='#A9A9A9',width=300,height=500).pack(side='right')
    title2 = Label(window, text='SENDER', bg='#A9A9A9',font=("Helvetica",35)).place(x=350,y=0)
    labe3 = Label(window, text="ASCII Karakter = "+ascii, bg='#A9A9A9',font=(30))
    labe3.place(x=320,y=200)
    label = Label(window, text="Data yang di kirim = \n"+data, bg='#A9A9A9',font=(30))
    label.place(x=320,y=220)
    labe2 = Label(window, text="metode yang di gunakan = "+metode, bg='#A9A9A9',font=(30))
    labe2.place(x=320,y=260)
    labe2 = Label(window, text="nilai parity "+jumlah_send, bg='#A9A9A9',font=(30))
    labe2.place(x=320,y=280)


    window.mainloop()

  
  
 

s = socket.socket() 
print ("Socket successfully created") 
port = 12345
  
s.bind(('', port)) 
print ("socket binded to %s" % (port)) 
# put the socket into listening mode 
s.listen(5) 
print ("socket is listening") 
  
 
while True: 
    # Establish connection with client. 
    c, addr = s.accept() 
    print('Got connection from', addr) 
   
    # Get data from client 
    data= c.recv(1024)
    metode= c.recv(1024)
    ascii= c.recv(1024)
    jumlah_send= c.recv(1024)

    print("data yang di kirim = "+data)
    # print("reminder yang di kirim = "+remi)
    
    if not data: 
        break
    
    #ubah data ke int
    datai = [int(x) for x in data]
    for y in datai:   
        jumlah += y
    if (metode =="y"):

        print("--metode yang di pilih adalah parity genap --")
        if(jumlah  %2 == 0):    
            print(jumlah)
        else:
            jumlah +=1
            print(jumlah)
    elif (metode =="n"):

        print("--metode yang di pilih adalah parity ganjil--")
        if(jumlah  %2 == 0): 
            jumlah +=1   
            print(jumlah)
        else:
            print(jumlah)
    
    jumlah = str(jumlah)

    if(data):
        tkint(data,metode,ascii,jumlah_send,jumlah) 
  
    c.close() 