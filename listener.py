import socket

class PortListener:

    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(('0.0.0.0', port))

    def get_packet(self):
        message, _ = self.server_socket.recvfrom(1024)
        return message
