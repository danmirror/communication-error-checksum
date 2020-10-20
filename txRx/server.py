import socket
from Tkinter import *


def tkint(ser,rem,rem1,ascii):


    window = Tk()
    window.title('GUI SERVER')
    window.geometry('600x500')

    data_ser = str(ser)
    remainder_ser = str(rem)
   # data_send = str(sen)
    remainder_sen = str(rem1)
    ascii_code = str(ascii)

    subFramel = Frame(window, bg='#F8F8F8', width=300,height=500).place(x=0,y=0)
    title1 = Label(window, text='SERVER',font=("Helvetica",35)).place(x=50,y=0)
    label = Label(window, text="Data Di Server = \n"+data_ser,font=(30))
    label.place(x=20,y=200)
    labe2 = Label(window, text="Remainder Decode Server = \n"+remainder_ser,font=(30))
    labe2.place(x=20,y=240)

    #title2
    subFrame2 = Frame(window, bg='#A9A9A9',width=300,height=500).pack(side='right')
    title2 = Label(window, text='SENDER', bg='#A9A9A9',font=("Helvetica",35)).place(x=350,y=0)
    labe3 = Label(window, text=" Nilai Kode ASCII Dari Karakter = \n"+ascii_code, bg='#A9A9A9',font=(30))
    labe3.place(x=320,y=200)
    label = Label(window, text="Data Di Server = \n"+data_ser, bg='#A9A9A9',font=(30))
    label.place(x=320,y=240)
    labe2 = Label(window, text="Remainder Encode Server = \n"+remainder_sen, bg='#A9A9A9',font=(30))
    labe2.place(x=320,y=280)


    window.mainloop()

  
  
def xor(a, b): 
   
    # initialize result 
    result = [] 

    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result)  
def mod2div(divident, divisor): 
    pick = len(divisor) 
    tmp = divident[0 : pick] 
   
    while pick < len(divident):    
        if tmp[0] == '1':    
            tmp = xor(divisor, tmp) + divident[pick]   
        else:   # If leftmost bit is '0'          
            tmp = xor('0'*pick, tmp) + divident[pick]     
        pick += 1
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    checkword = tmp 
    return checkword 
def decodeData(data, key): 
   
    l_key = len(key) 
 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key)  
    return remainder 
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
    print (data)
    
    if not data: 
        break
  
  
  
    c.close() 