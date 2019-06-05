from telemetry import GameTelemetry
import struct

class CodeMasters(GameTelemetry):
    # using https://docs.google.com/spreadsheets/d/1eA518KHFowYw7tSMa-NxIFYpiWe5JXgVVQ_IMs7BVW0/edit#gid=0
    def __init__(self):
        self.lap_time = 0
        self.speed = 0
        self.gear = 0
        self.rpm = 0
        self.rpm_max = 0

    def get_speed(self):
        return self.speed

    def get_rev(self):
        return [self.rpm, self.rpm_max]
    
    def get_gear(self):
        return self.gear

    def update(self, packet):
        NUM_ITEMS = 64  # game specific
        SIZE_ITEM = 4
        
        data = []

        for i in range(NUM_ITEMS):
            data.append(struct.unpack('f', packet[SIZE_ITEM * i : SIZE_ITEM * i + SIZE_ITEM])[0])

        self.lap_time = data[0 // SIZE_ITEM]
        self.speed = data[28 // SIZE_ITEM]
        self.gear = data[132 // SIZE_ITEM]
        self.rpm = data[148 // SIZE_ITEM]
        self.rpm_max = data[252 // SIZE_ITEM]
