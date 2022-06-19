"""
Pomiary, pomiary...
"""

import time
import serial.tools.list_ports
from datetime import datetime

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial()

port_list = []
first_loop = True

for port in ports:  # wyswietla wszystkie dostepne porty
    port_list.append(str(port))
    print(str(port))

serial_inst.baudrate = 9600
serial_inst.port = 'COM4'
serial_inst.open()  # otwiera port i pozwala nasłuchiwać

while True:
    if serial_inst.in_waiting:  # jesli są jakieś dane do odbioru to je pobiera
        packet = serial_inst.readline().decode('utf').rstrip('\n')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, end='; ')
        print(packet)
        with open('measurements.txt', 'a') as f:
            f.write(current_time + '; ' + packet)
    time.sleep(0.001)

