import serial
import time


class SmartSwitch:
    def __init__(self, port='COM1'):

        self.CmdSwitchToChannelA = bytearray([0x1B, 0x02, 0x02, 0x04, 0x0D, 0x1B, 0x02, 0x30, 0x41, 0x0D])
        self.CmdSwitchToChannelB = bytearray([0x1B, 0x02, 0x02, 0x04, 0x0D, 0x1B, 0x02, 0x30, 0x42, 0x0D])
        self.CmdSwitchToChannelC = bytearray([0x1B, 0x02, 0x02, 0x04, 0x0D, 0x1B, 0x02, 0x30, 0x43, 0x0D])
        self.CmdSwitchToChannelD = bytearray([0x1B, 0x02, 0x02, 0x04, 0x0D, 0x1B, 0x02, 0x30, 0x44, 0x0D])
        self.CmdSwitchToChannelE = bytearray([0x1B, 0x02, 0x02, 0x04, 0x0D, 0x1B, 0x02, 0x30, 0x45, 0x0D])
        self.CmdSwitchToChannelF = bytearray([0x1B, 0x02, 0x02, 0x04, 0x0D, 0x1B, 0x02, 0x30, 0x46, 0x0D])
        self.CmdReadCurrentTemp = b't\r'
        self.CmdReadSetTemp = b's\r'
        self.CmdSetTemp = b's='     # do nastepnej wersji
        

        self.CurrentTemp = None
        self.SetTemp = None

        try:
            self.SmartSwitch = serial.Serial(port, 2400, timeout=1)
        except serial.SerialException:
            print('Nie można otworzyć portu dla SmartSwitch.')
            self.SmartSwitch = None

        else:
            print('Połączenie z SmartSwitch - OK')

    def switch_to_channel_a(self):
        self.SmartSwitch.write(self.CmdSwitchToChannelA)

    def switch_to_channel_b(self):
        self.SmartSwitch.write(self.CmdSwitchToChannelB)

    def switch_to_channel_c(self):
        self.SmartSwitch.write(self.CmdSwitchToChannelC)

    def switch_to_channel_d(self):
        self.SmartSwitch.write(self.CmdSwitchToChannelD)

    def switch_to_channel_e(self):
        self.SmartSwitch.write(self.CmdSwitchToChannelE)

    def switch_to_channel_f(self):
        self.SmartSwitch.write(self.CmdSwitchToChannelF)

    def read_current_temp(self):
        self.SmartSwitch.flushInput()
        self.SmartSwitch.write(self.CmdReadCurrentTemp)
        time.sleep(0.5)
        try:
            self.CurrentTemp = str(self.SmartSwitch.readline()[4:15].decode())
        except:
            self.CurrentTemp = "Błędna odpowiedź termostatu"
        if len(self.CurrentTemp) == 0:
            return "Błąd połączenia"
        else:
            return self.CurrentTemp

    def read_set_temp(self):
        self.SmartSwitch.flushInput()
        self.SmartSwitch.write(self.CmdReadSetTemp)
        time.sleep(0.5)
        try:
            self.SetTemp = str(self.SmartSwitch.readline()[4:15].decode())
        except:
            self.SetTemp = "Błędna odpowiedź termostatu"
        if len(self.SetTemp) == 0:
            return "Błąd połączenia"
        else:
            return self.SetTemp

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
