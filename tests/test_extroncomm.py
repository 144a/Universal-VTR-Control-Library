import sys
import os
import pytest
from unittest.mock import patch, Mock
from uvcl.comms.extroncomm import ExtronComm
from uvcl.exceptions import InvalidPortError, InvalidParityError
import requests

# Add the project directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Test fixture for ExtronComm instance
@pytest.fixture
def extron_comm_instance():
    return ExtronComm("192.168.1.1", 1)

# Parameterized tests for sendCommand function
@pytest.mark.parametrize("target_port, command, expected_status_code, expected_text", [
    (5, "test_command", 200, "Success"),
])
def test_send_command_valid(extron_comm_instance, target_port, command, expected_status_code, expected_text):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.status_code = expected_status_code
        mock_response.text = expected_text
        mock_get.return_value = mock_response

        response = extron_comm_instance.sendCommand(target_port, command)
        assert response.status_code == expected_status_code
        assert response.text == expected_text

@pytest.mark.parametrize("target_port, command", [
    (10, "test_command"),
    (0, "test_command"),
])
def test_send_command_invalid_port(extron_comm_instance, target_port, command):
    with pytest.raises(InvalidPortError):
        extron_comm_instance.sendCommand(target_port, command)

def test_send_command_request_exception(extron_comm_instance):
    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        response = extron_comm_instance.sendCommand(5, "test_command")
        assert response is None

# Parameterized tests for configureUnit function
@pytest.mark.parametrize("target_port, baudrate, parity, data_bits, stop_bits, expected_status_code, expected_text", [
    (5, 38400, "Odd", 8, 1, 200, "Success"),
    (5, 38400, "Even", 8, 1, 200, "Success"),
    (5, 38400, "None", 8, 1, 200, "Success")
])
def test_configure_unit_valid(extron_comm_instance, target_port, baudrate, parity, data_bits, stop_bits, expected_status_code, expected_text):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.status_code = expected_status_code
        mock_response.text = expected_text
        mock_get.return_value = mock_response

        response = extron_comm_instance.configureUnit(target_port, baudrate, parity, data_bits, stop_bits)
        assert response.status_code == expected_status_code
        #assert response.text == expected_text

@pytest.mark.parametrize("target_port, baudrate, parity, data_bits, stop_bits", [
    (10, 38400, "Odd", 8, 1),
    (0, 38400, "Odd", 8, 1),
])
def test_configure_unit_invalid_port(extron_comm_instance, target_port, baudrate, parity, data_bits, stop_bits):
    with pytest.raises(InvalidPortError):
        extron_comm_instance.configureUnit(target_port, baudrate, parity, data_bits, stop_bits)

@pytest.mark.parametrize("target_port, baudrate, parity, data_bits, stop_bits", [
    (5, 38400, "Invalid", 8, 1),
])
def test_configure_unit_invalid_parity(extron_comm_instance, target_port, baudrate, parity, data_bits, stop_bits):
    with pytest.raises(InvalidParityError):
        extron_comm_instance.configureUnit(target_port, baudrate, parity, data_bits, stop_bits)

def test_configure_unit_request_exception(extron_comm_instance):
    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        response = extron_comm_instance.configureUnit(5, 38400, "Odd", 8, 1)
        assert response is None