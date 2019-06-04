class GameTelemetry:

    def get_cur_speed(self):
        raise NotImplementedError

    def get_cur_rev(self):
        raise NotImplementedError
        
    def get_cur_gear(self):
        raise NotImplementedError

    def update(self, packet):
        raise NotImplementedError
