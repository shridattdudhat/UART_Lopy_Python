import pycom
from time import *
#defining function
def getData():
    uart1=UART(1, 9600) 
    uart1.inti(9600,bits=8,parity=None,stop=1)
    sleep(1)
    data=uart1.read(10)
    sleep(1)
    print('Received bytes: ', data)
