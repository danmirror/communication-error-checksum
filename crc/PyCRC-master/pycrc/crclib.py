#!/usr/bin/env python
import random

class Converter(object):

    def dec2bin(self, decimal):
    
        if type(decimal).__name__ == 'str':
            print "Error type : Not a integer"
            return 0

        digit = 1
        binary = 0

        decimal = int(decimal)

        while decimal != 0:
            binary = binary + (decimal%2) * digit
            decimal = decimal/2
            digit = digit * 10
        
        return str(binary)

    def bin2dec(self, binary):

        if type(binary).__name__ == 'int':
            print "Error type : Not a string"
            return 0
        
        digit = 1
        decimal = 0

        binary = int(binary)

        while binary != 0:
            decimal = decimal + (binary%10) * digit
            binary = binary/10
            digit = digit * 2
        
        return decimal

    def count_bit(self, value):
    
        if type(value).__name__ == 'int':
            binary = self.dec2bin(value)
            num_bits = len(binary)
        else:     
            num_bits = len(value)

        return num_bits


class Sender(Converter):

    def __init__(self, dataword, divisor):
        
        self.divisor = self.bin2dec(divisor)
        self.dataword = self.bin2dec(dataword)
        self.remainder = 0
        self.codeword = 0
        self.arg_dataword = 0
    
    def __getArgdataword(self):
        
        self.arg_dataword = self.dataword << self.count_bit(self.divisor)-1
        
        return self.arg_dataword

    def __generator(self):
        arg_bit = self.count_bit(self.dec2bin(self.arg_dataword))
        div_bit = self.count_bit(self.dec2bin(self.divisor))
        
        padded_bit = arg_bit - div_bit
        divisor_shift = self.divisor << padded_bit

        result = self.arg_dataword
        while(True):

            result = result ^ divisor_shift
            #print self.dec2bin(result)

            padded_bit = self.count_bit(self.dec2bin(result)) - div_bit
            if padded_bit < 0:
                break
            divisor_shift = self.divisor << padded_bit

        self.remainder = result
        
        return self.remainder

    def __getCodeword(self):

        self.codeword = self.arg_dataword | self.remainder
        
        return self.codeword

    def send(self):
        self.arg_dataword = self.__getArgdataword()
        self.remainder = self.__generator()
        self.codeword = self.__getCodeword()

        def converter():
            self.arg_dataword2 = self.dec2bin(self.arg_dataword)
            self.remainder2 = self.dec2bin(self.remainder)
            self.codeword2 = self.dec2bin(self.codeword)

        converter()


class Receiver(Converter):
    
    def __init__(self, codeword, divisor):
        
        self.codeword = codeword
        self.divisor = self.bin2dec(divisor)
        self.syndrome = 0
        self.rx_dataword = 0
        self.discard = False

    def __getDataword(self):
        
        self.rx_dataword = self.codeword >> self.count_bit(self.divisor)-1
        return self.rx_dataword

    def __checker(self):
        code_bit = self.count_bit(self.dec2bin(self.codeword))
        div_bit = self.count_bit(self.dec2bin(self.divisor))
        
        padded_bit = code_bit - div_bit
        divisor_shift = self.divisor << padded_bit

        result = self.codeword
        while(True):

            result = result ^ divisor_shift
            #print self.dec2bin(result)

            padded_bit = self.count_bit(self.dec2bin(result)) - div_bit
            if padded_bit < 0:
                break
            divisor_shift = self.divisor << padded_bit

        self.syndrome = result
        
        return self.syndrome

    def __decision(self):
        self.rx_dataword = self.__getDataword()

        
        if self.syndrome == 0:
            
            return False, self.rx_dataword
        else:

            return True, self.rx_dataword

    def receive(self):
        self.syndrome = self.__checker()
        self.discard, self.rx_dataword = self.__decision()

        def converter():
            self.syndrome2 = self.dec2bin(self.syndrome)
            self.rx_dataword2 = self.dec2bin(self.rx_dataword)

        converter()            


class Channel(Converter):
    
    def __init__(self, codeword, rate=0.3):

        self.codeword = codeword
        self.rate = rate
        self.rand = random.randint(1,101)
        self.noise = random.randint(1, self.codeword)
        self.ch_codeword = 0
        self.__passed()
        
    def __passed(self):
        
        if self.rand > self.rate*100:
            self.ch_codeword = self.codeword
        
        elif self.rand > self.rate*100*0.5 and self.rand <= self.rate*100:
            self.ch_codeword = self.codeword | self.noise
        
        else:
            self.ch_codeword = self.codeword ^ self.noise

        self.ch_codeword2 = self.dec2bin(self.ch_codeword)

