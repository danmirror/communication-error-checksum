PyCRC
=====

This Program is my study on the course named Communications Network.

## Description 
------
This is the cyclic redundancy check (CRC) Simulate, if you don't know how it works take a look on [Cyclic Redundancy Check](http://en.wikipedia.org/wiki/Cyclic_redundancy_check).

CRC Sender need to encode the dataword into codeword.
CRC Receiver need to determine the received codeword if the received codeword been corrupted by noise, then discard it. Otherwise received the dataword.

The crclib provided some features:

* Sender Class:
    * Generate augmented dataword method.
    * Generate remainder method.
    * Generate codeword method.
    * Send codeword method

* Receiver Class:
    * Generate syndrome method.
    * To decide whether discart received dataword or not method.
    * Get dataword back from codeword method.

* Unreliable Channel Class:
    * Generate random noise by input error rate parameter.
    
    
## CRC detection simulate Example in main program
------
```
#!/usr/bin/env python
#from pycrc.crclib import Sender, Receiver, Channel
from pycrc.crclib import *
def main():
#-----------------------------------------------------------------------------
#Sender

    divisor = str(raw_input("Input divisor in binary type: "))
    #user_dataword = str(raw_input("Input dataword in binary type: "))
    user_dataword = '1001'

    print "\nSender:"
    
    sender = Sender(bin2dec(user_dataword), divisor)
    sender.send()
    
    print "arg_dataword:", sender.arg_dataword2
    print "remainder:", sender.remainder2
    print "codeword:", sender.codeword2
 
#-----------------------------------------------------------------------------
#Channel

    print "\nChannel:"

    channel = Channel(sender.codeword)
    print "Throgh to the channel get channel codeword:", dec2bin(channel.ch_codeword)
     
#-----------------------------------------------------------------------------
#Receiver

    print "\nReceiver:"

    receiver = Receiver(channel.ch_codeword, divisor)

    receiver.receive()

    print "syndrome:", receiver.syndrome2
    print "Discard or not?", receiver.discard
    print "rx_dataword:", receiver.rx_dataword2

if __name__ == '__main__':
    main()

```

##Contact
-----
Email: <ireri339@gmail.com>