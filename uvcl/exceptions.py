

# ExtronComm Exceptions
class InvalidPortError(Exception):
    """Raise when extron device port is invalid/out of range"""
    
class InvalidParityError(Exception):
    """Raise when parity argument is invalid"""