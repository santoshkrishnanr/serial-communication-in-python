import time
import serial     
import datetime     
ser = serial.Serial(
              
	port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0
                
while 1:
	now=datetime.datetime.now()
        y=now.strftime("%S")
        x=ser.readline()
        print x,y