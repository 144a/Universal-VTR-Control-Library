import serial
import io
import time
class ExtronComm:
    ser = None
    def __init__(self, serial_port, baudrate = 38400):
        # Create Serial Object
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = serial_port