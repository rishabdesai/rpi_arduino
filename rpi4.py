#! /usr/bin/env pyyhon3

# Sending data from Raspberry Pi to Arduino board
import serial  
import time

ser = serial.Serial('/dev/ttyACM0',115200,timeout=1.0)   #open serial communication
time.sleep(3) #wait for 3 seconds
ser.reset_input_buffer() # refresh buffer
print("Serial OK")

try:
    while True:
        time.sleep(1)
        print("sending message to Arduino board")
        ser.write("hello from RaspberryPi!!!\n".encode('utf-8'))
        while ser.in_waiting <=0:
            time.sleep(0.01)
        response = ser.readline().decode('utf-8').rstrip()
        print(response)
except KeyboardInterrupt:
    print("close the serial comm")
    ser.close()


ser.close()
