# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin, UART
from time import sleep_ms

class RYLR998:
    def __init__(self, port_num, tx_pin='', rx_pin=''):
        if tx_pin=='' and rx_pin=='':
            self._uart = UART(port_num)
        else:
            self._uart = UART(port_num, tx=tx_pin, rx=rx_pin)
                
    def cmd(self, lora_cmd):
        self._uart.write('{}\r\n'.format(lora_cmd))
        while(self._uart.any()==0):
            pass
        reply = self._uart.readline()
        print(reply.decode().strip('\r\n'))
    
    def test(self):
        self._uart.write('AT\r\n')
        while(self._uart.any()==0):
            pass
        reply = self._uart.readline()
        print(reply.decode().strip('\r\n'))

    def set_addr(self, addr):
        self._uart.write('AT+ADDRESS={}\r\n'.format(addr))
        while(self._uart.any()==0):
            pass
        reply = self._uart.readline()
        print(reply.decode().strip('\r\n'))
        print('Addreset to:{}\r\n'.format(addr))


    def send_msg(self, addr, msg):
        self._uart.write('AT+SEND={},{},{}\r\n'.format(addr,len(msg),msg))
        while(self._uart.any()==0):
            pass
        reply = self._uart.readline()
        print(reply.decode().strip('\r\n'))
        
    def read_msg(self):
        if self._uart.any()==0:
            print('Nothing to show.')
        else:
            msg = ''
            while(self._uart.any()):
                msg = msg + self._uart.read(self._uart.any()).decode()
            print(msg.strip('\r\n'))
            
lora = RYLR998(1,rx_pin=5,tx_pin=4) # Sets the UART port to be use
sleep_ms(100)
lora.set_addr(2)  # Sets the LoRa address

