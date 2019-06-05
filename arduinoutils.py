import struct
from serial import Serial

class ArduinoCommunication:
    def __init__(self, device, baud):
        self.device = device
        self.baud_rate = baud
        self.serial_comm = Serial(device, baud)
    
    def send(self, payload):
        bytes_payload = []
        for fl in payload:
            bytes_payload += struct.pack('f', fl)

        print(bytes_payload)
        print(payload)
        self.serial_comm.write(bytes_payload)
        self.serial_comm.flush()

    def receive(self):
        return self.serial_comm.read()
