import socket
import io
import time
class LanComm:
    HOST = "192.168.0.1"
    PORT = 53484
    sock = None
    def __init__(self, serial_port, baudrate = 38400):
        self.sock = self.connect()
        
    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        return s
    
    def sendCommand(self, command):
        self.sock.send(command)
        data = self.sock.recv(1024)
        return data