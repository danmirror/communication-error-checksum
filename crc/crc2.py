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