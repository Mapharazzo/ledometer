class GameTelemetry:
    t_time = 0
    t_speed = 0
    t_throttle = 0
    t_steer = 0
    t_brake = 0
    t_clutch = 0
    t_gear = 0
    t_engine_rate = 0
    t_drs = 0
    t_max_engine_rate = 0

    def get_cur_speed(self):
        raise NotImplementedError

    def get_cur_rev(self):
        raise NotImplementedError
        
    def get_cur_gear(self):
        raise NotImplementedError

    def update(self, packet):
        raise NotImplementedError
