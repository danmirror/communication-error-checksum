# Python3 code to get parity. 
  
# Function to get parity of number n.  
# It returns 1 if n has odd parity,  
# and returns 0 if n has even parity 
def getParity( n ): 
    parity = 0
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    return parity 
  
# Driver program to test getParity() 
n = 0
print ("Parity of no ", n," = ", 
     ( "odd" if getParity(n) else "even")) 