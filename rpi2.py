#! /usr/bin/env pyyhon3

import serial  
import time

ser = serial.Serial('/dev/ttyACM0',115200,timeout=1.0)   #open serial communication
time.sleep(3) #wait for 3 seconds
ser.reset_input_buffer() # refresh buffer
print("Serial OK")

try:
    while True:
        time.sleep(0.1)
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
except KeyboardInterrupt:
    print("close the serial comm")
    ser.close()


ser.close()
