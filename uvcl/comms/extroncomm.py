import requests
import io
import time
from uvcl.exceptions import InvalidPortError, InvalidParityError

class ExtronComm:
    base_url = None
    serial_port = 0
    def __init__(self, ip_address, serial_port):
        # Create Serial Object
        self.base_url = f'http://{ip_address}/'
        self.serial_port = serial_port
        
    def sendCommand(self, target_port: int, command: str, timeout=10):
        """Sends a command to an Extron IP Link device via a URL.

        This function constructs a URL based on the target port and command, then sends a GET request
        to the Extron device. If the target port is not within the valid range (1-9), the function 
        raises an InvalidPortError. If there is an error in sending the command, it prints the error.

        Args:
            target_port (int): The target port number on the Extron device (must be between 1 and 9).
            command (str): The command string to send to the Extron device.
            timeout (int, optional): The timeout duration for the GET request in tens of milliseconds. 
                                    Default is 10 (i.e., 100 milliseconds). The maximum value is 32767.

        Returns:
            response: The response object from the GET request if successful.
        """
        if target_port < 1 or target_port > 9:
            raise InvalidPortError
        url = self.base_url + f'?cmd=W0{target_port}%2A2000%2A{timeout}RS|' + command
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.RequestException as e:
            print("Error sending command:", e)
            return None
        return response
    
    def configureUnit(self, target_port: int, baudrate=38400, parity='Odd', data_bits=8, stop_bits=1):
        """Configures the unit settings for a specified port on an Extron device.

        This function constructs a URL based on the target port and configuration parameters, then sends 
        a GET request to the Extron device to configure the unit settings. If the target port is not 
        within the valid range (1-9), the function raises an InvalidPortError. If the parity value is 
        not one of the accepted values ('Odd', 'Even', 'None'), the function raises an InvalidParityError.
        If there is an error in sending the command, it prints the error.

        Parameters:
        target_port (int): The target port number on the Extron device (must be between 1 and 9).
        baudrate (int, optional): The baud rate for communication. Default is 38400.
        parity (str, optional): The parity setting for communication. Must be 'Odd', 'Even', or 'None'. Default is 'Odd'.
        data_bits (int, optional): The number of data bits. Default is 8.
        stop_bits (int, optional): The number of stop bits. Default is 1.

        Returns:
        response: The response object from the GET request if successful, or None if there was an error.
        """
        parity_dict = {'Odd' : 'O', 'Even' : 'E', 'None' : 'N'}
        if target_port < 1 or target_port > 9:
            raise InvalidPortError
        if parity not in parity_dict:
            raise InvalidParityError
        url = self.base_url + f'?cmd=W0{target_port}%2A{baudrate}%2C{parity}%2C{data_bits}%2C{stop_bits}CP|'
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.RequestException as e:
            print("Error sending command:", e)
            return None
        return response
    
if __name__ == '__main__':
    ex = ExtronComm('192.168.254.30', 1)
    rep = ex.sendCommand(1, 'ff00ff')
    print(rep.status_code)