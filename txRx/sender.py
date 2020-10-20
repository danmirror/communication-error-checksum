import socket                
   
def xor(a, b): 
   
  
    result = [] 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
    return ''.join(result) 
# Performs Modulo-2 division 
def mod2div(divident, divisor): 
   
    pick = len(divisor) 
    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
   
        if tmp[0] == '1': 
            tmp = xor(divisor, tmp) + divident[pick]   
        else:           
            tmp = xor('0'*pick, tmp) + divident[pick] 
        pick += 1
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    checkword = tmp 
    return checkword 
   

def encodeData(data, key): 
    global remainder
    l_key = len(key) 
 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
   
    # Append remainder in the original data 
    codeword = data + remainder 
    
    print ("code word setelah encode = "+codeword)
    return codeword   
s = socket.socket()          
port = 12345               
s.connect(('192.168.1.10', port)) 
  
input_string = raw_input("Data yang akan anada kirim->") 
data =(''.join(format(ord(x), 'b') for x in input_string)) 
print ("data -> "+data) 
key = "1001"
  
ans =encodeData(data,key) 
s.sendall(ans) 
s.sendall(remainder)
s.sendall(data)
#print (s.recv(1024))
print ("remainder setelah encode = "+remainder)
s.close()