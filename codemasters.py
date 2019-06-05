from telemetry import GameTelemetry
import struct

class CodeMasters(GameTelemetry):
    def __init__(self):
        pass

    def update(self, packet):
        NUM_ITEMS = 64  # game specific
        SIZE_ITEM = 4
        data = []

        for i in range(NUM_ITEMS):
            data.append(struct.unpack('f', packet[4*i : 4*i + 4])[0])
        
        # using https://docs.google.com/spreadsheets/d/1eA518KHFowYw7tSMa-NxIFYpiWe5JXgVVQ_IMs7BVW0/edit#gid=0

        self.t_time = data[0 // SIZE_ITEM]
        self.t_speed = data[28 // SIZE_ITEM]
        self.t_throttle = data[116 // SIZE_ITEM]
        self.t_steer = data[120 // SIZE_ITEM]
        self.t_brake = data[124 // SIZE_ITEM]
        self.t_clutch = data[128 // SIZE_ITEM]
        self.t_gear = data[132 // SIZE_ITEM]
        self.t_engine_rate = data[148 // SIZE_ITEM]
        self.t_drs = data[168 // SIZE_ITEM]
        self.t_max_engine_rate = data[252 // SIZE_ITEM]

    def get_cur_rev(self):
        return [self.t_engine_rate, self.t_max_engine_rate]
