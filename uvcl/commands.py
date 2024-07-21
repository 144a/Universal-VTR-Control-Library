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
    'Local Enable' : ['00 1D', 'Ack']
}