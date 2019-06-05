import codemasters
import listener
import sys
import serial
import arduinoutils

CODEMASTERS_GAMES = ['rally', 'rally2', 'f1']
BAUD_RATE = 115200

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python ./ledometer.py <GAME> <PORT> <DEVICE>")
        exit(1)

    port = int(sys.argv[2])
    device = sys.argv[3]
    game_listener = listener.PortListener(port)
    arduino_comm = arduinoutils.ArduinoCommunication(device, BAUD_RATE)
    if sys.argv[1] in CODEMASTERS_GAMES:
        telemetry_client = codemasters.CodeMasters()

    while True:
        new_packet = game_listener.get_packet()
        telemetry_client.update(new_packet)
        arduino_comm.send(telemetry_client.get_rev())
