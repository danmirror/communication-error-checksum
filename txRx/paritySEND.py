import socket                
jumlah = 0  


s = socket.socket()          
port = 12345               
s.connect(('127.0.0.1', port)) 
  
input_string = raw_input("Data yang akan anda kirim->") 
data =(''.join(format(ord(x), 'b') for x in input_string)) 
print ("data -> "+data) 
input_metode = raw_input("pilih parity genap (y) atau parity ganjil (n)->") 

#ubah data ke int
datai = [int(x) for x in data]
#mencari jumlah nilai
print(data)
for y in datai:   
    jumlah += y
if (input_metode =="y"):

    print("--metode yang di pilih adalah parity genap --")
    if(jumlah  %2 == 0):    
        print(jumlah)
    else:
        jumlah +=1
        print(jumlah)
elif (input_metode =="n"):

    print("--metode yang di pilih adalah parity ganjil--")
    if(jumlah  %2 == 0): 
        jumlah +=1  
        print(jumlah)
    else:
        print(jumlah)

    
s.sendall(data) 
s.sendall(input_metode)
s.sendall(input_string)
s.sendall(str(jumlah))

s.close()