import socket

UDP_IP = "192.168.100.2"
UDP_PORT = 5227
MESSAGE = b"Hello, World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))