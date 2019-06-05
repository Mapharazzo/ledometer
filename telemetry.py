class GameTelemetry:

    def get_speed(self):
        """
        Get current speed of the vehicle as float in KM/H.
        """
        raise NotImplementedError

    def get_rev(self):
        """
        Get current and max RPM value in a tuple of floats.\n
        [0] - Current value\n
        [1] - Max value\n
        """
        raise NotImplementedError
        
    def get_gear(self):
        """
        Return current gear of the vehicle as a float.\n
        -1 - Reverse\n
        0 - Neutral\n
        1:X - Normal gears\n
        """
        raise NotImplementedError

    def update(self, packet):
        """
        Updates the state with new info from the packet.\n
        packet - Packet with info to update from.
        """
        raise NotImplementedError
