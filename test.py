from codemasters import CodeMasters
from listener import PortListener

port_list = PortListener(20777)
game_tel = CodeMasters()

while True:
    game_tel.update(port_list.get_packet())
    print(game_tel.get_rev(), game_tel.get_speed(), game_tel.get_gear())