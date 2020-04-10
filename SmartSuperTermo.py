import serial
import time


class SmartSuperTermo:
    def __init__(self, port='COM8'):

        self.CmdIDN                 = b'*IDN?\r'
        self.CmdReadLast            = b'FETC?\r'
        
        self.CurrentTemp = None
        self.IDN = None
        self.port = port

        try:
            self.SmartSuperTermo = serial.Serial(port, 9600, timeout=1)
        except serial.SerialException:
            print('Nie można otworzyć portu dla SmartSuperTermo.')
            self.SmartSuperTermo = None

        else:
            print('Połączenie z SuperTermo - OK')

    def read_idn(self):
        self.SmartSuperTermo.flushInput()
        self.SmartSuperTermo.write(self.CmdIDN)
        time.sleep(0.5)
        try:
            self.IDN = str(self.SmartSuperTermo.readline()[0:11].decode())
        except:
            self.IDN = "Błędna odpowiedź termostatu"
        if len(self.IDN) == 0:
            return "Błąd połączenia"
        else:
            return self.IDN

    def read_current_temp(self):
        self.SmartSuperTermo.flushInput()
        self.SmartSuperTermo.write(self.CmdReadLast)
        time.sleep(0.5)
        try:
            self.CurrentTemp = str(self.SmartSuperTermo.readline()[0:11].decode())
        except:
            self.CurrentTemp = "Błędna odpowiedź termostatu"
        if len(self.CurrentTemp) == 0:
            return "Błąd połączenia"
        else:
            return self.CurrentTemp
# TESTY

# time.sleep(1)
# SmartSwitch.flushInput()
# SmartSwitch.write(b't\r')
# time.sleep(0.1)
# print(str(SmartSwitch.readline().decode()))
#
# SmartSwitch.write(CommandSwitchToChannelB)
# time.sleep(1)
# SmartSwitch.flushInput()
# SmartSwitch.write(b't\r')
# time.sleep(0.1)
# print(str(SmartSwitch.readline().decode()))
