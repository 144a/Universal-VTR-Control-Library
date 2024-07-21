# Command structure:
#
#|-------------------|-------------------|-------------------|-------------------|
#| CMD1 / Data Count |       CMD 2       |  Data n (n=0~15)  |      Checksum     |
#|  MSD      LSD     |                   |                   |                   |
#|-------------------|-------------------|-------------------|-------------------|
#       1 Byte              1 Byte             1-n Bytes             1 Byte       
# Checksum 
# CMD 1 
# Determines the function/type of command being sent/recieved
CMD1 = {
    'SYSTEM CONTROL' : 0, # To VTR
    'SYSTEM CONTROL RETURN' : 1, # From VTR
    'TRANSPORT CONTROL' : 2, # To VTR
    'SELECT CONTROL' : 4, # To VTR
    'SENSE REQUEST' : 6, # To VTR
    'SENSE RETURN' : 7, # From VTR
}

# Command table is from the DVR-2000/2100 documentation
CMD2 = {
    'Local Disable' : ['00 0c', 'Ack'],
    'Device Type Request' : ['12 11', 'Device Type'],
    'Local Enable' : ['00 1D', 'Ack'],
    'Stop' : ['20 00', 'Ack'],
    'Play' : ['20 01', 'Ack'],
    'Record' : ['20 02', 'Ack'],
    'Standby Off' : ['20 04', 'Ack'],
    'Standby On' : ['20 05', 'Ack'],
    'Eject' : ['20 0F', 'Ack'],
    'Fast Fwd' : ['20 10', 'Ack'],
    'Jog Fwd' : ['2X 11', 'Ack'],
    'Var Fwd' : ['2X 12', 'Ack'],
    'Shuttle Fwd' : ['2X 13', 'Ack'],
    'Rewind' : ['20 20', 'Ack'],
    'Jog Rev' : ['2X 21', 'Ack'], 
    'Var Rev' : ['2X 22', 'Ack'],
    'Shuttle Rev' : ['2X 23', 'Ack'],
}