from machine import UART
import machine
import os
import pycom
import time
uart = UART(0, baudrate=115200)
os.dupterm(uart)
machine.main('main.py')
