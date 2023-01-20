# -*- coding: utf-8 -*-
from gsmmodem.modem import GsmModem

PORT = '/dev/ttyUSB0'
#BAUDRATE = 115200
BAUDRATE = 9600
PIN = 1909
#print help(GsmModem)
modem = GsmModem(PORT, BAUDRATE)
modem.connect(PIN)
print (modem.sendSms( '04129027646', 'holamundo'))

print('Waiting for SMS message...')