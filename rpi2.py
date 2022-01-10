#! /usr/bin/env pyyhon3

import serial  
import time

ser = serial.Serial('/dev/ttyACM0',115200,timeout=1.0)   #open serial communication
time.sleep(3) #wait for 3 seconds
ser.reset_input_buffer() # refresh buffer
print("Serial OK")
ser.close()
