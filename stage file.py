from space_network_lib import *
import time

space_net = SpaceNetwork(2)


class Satellite(SpaceEntity):
    def __init__(self, name, distance_from_earth):
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet: Packet):
        return f"{self.name} Received: {packet}"


def attempt_transmission(packet):
    try:
        space_net.send(packet)
    except TemporalInterferenceError:
        print("Interference, waiting ...")
        time.sleep(2)
        attempt_transmission(packet)
    except DataCorruptedError:
        print("corrupted, retrying...")
        attempt_transmission(packet)


sat1 = Satellite("satellite1", 100)
sat2 = Satellite("satellite2", 200)
new_message = Packet("i found aliens", sat1, sat2)
attempt_transmission(new_message)
