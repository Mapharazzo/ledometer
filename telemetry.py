class GameTelemetry:
    
    def get_speed(self):
        raise NotImplementedError

    def get_rev(self):
        raise NotImplementedError
        
    def get_gear(self):
        raise NotImplementedError

    def update(self, packet):
        raise NotImplementedError
