import listener as lst
import struct

listener = lst.PortListener(5227)

num_items = 64

data = struct.unpack('{}f'.format(num_items), listener.get_packet())

print(data)