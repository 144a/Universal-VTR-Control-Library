import serial
import io
import time
class SerialComm:
    ser = None
    def __init__(self, serial_port, baudrate=38400):
        # Create Serial Object
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = serial_port

    def connect(self):
        """Opens serial connection to VTR"""
        try:
            self.ser.open()
        except:
            print ("Error connecting to Serial Port")
            
    def close(self):
        """Closes serial connection to VTR"""
        self.ser.close()
    
    def flush(self):
        """Flushes all current serial data"""
        self.ser.flush()
        
    def writeCommand(self, command):
        """ Sends correct byte array for corresponding command """
        pass
    
    def repeatCommand(self, command, reps):
        pass
    
    def sendCommand(self, inp_str):
        pass
    