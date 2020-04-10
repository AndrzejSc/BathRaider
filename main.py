from statistics import mode
# -*- coding: utf-8*-

#import serial
import time
import datetime
from bs4 import BeautifulSoup
import sys
import SmartSwitch
import SmartSuperTermo

# Opis połączeń SmartSwitch
# Port A - Termostat wodny
# Port B - Termostat spirytus
# Port C - Termostat olej
# Port D - Termostat sól

# Otwarcie połączenia do SmartSwitcha
SmartSwitch = SmartSwitch.SmartSwitch('COM1')
if SmartSwitch.SmartSwitch is None:
    sys.exit()

# Otwarcie połączenia do SmartSuperTermo
SuperTermo = SmartSuperTermo.SmartSuperTermo('COM8')
if SuperTermo.SmartSuperTermo is None:
    sys.exit()


#SmartSwitch.switch_to_channel_a()
#print(SmartSwitch.read_current_temp())
#SmartSwitch.switch_to_channel_b()
#print(SmartSwitch.read_current_temp())

# open html files and save to soup object
path = '//Comw02/obieg_dokumentow/Temperatura/Odczyt_z_termostatow.html'
try:
    html_file = open(path, mode='r')    # Otwieram plik html z serwera
    soup = BeautifulSoup(html_file.read(), features='html.parser')  #zapisuje zawarotsc pliku html do obiektu soup
    print("HTML read OK")
    html_file.close()                   # Zamykam plik html
except IOError:
    print("Błąd otwarcia pliku html")
    sys.exit()

while True:

    # Aktualizacja pliku html wczytanego do obiektu soup
    # Zmiana daty i godziny
    dataString = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    for tag in soup.find_all(id='time'):
        tag.string.replace_with(dataString)

    # Zmiana html aktualnej  i zadanej temperatury wody
    SmartSwitch.switch_to_channel_a()
    for tag in soup.find_all(id='CurrentWaterTemp_html'):
        tag.string.replace_with(SmartSwitch.read_current_temp())
    for tag in soup.find_all(id='SetWaterTemp_html'):
        tag.string.replace_with(SmartSwitch.read_set_temp())

    # Zmiana html aktualnej i zadanej temperatury spiritu
    SmartSwitch.switch_to_channel_b()
    for tag in soup.find_all(id='CurrentSpiritTemp_html'):
        tag.string.replace_with(SmartSwitch.read_current_temp())
    for tag in soup.find_all(id='SetSpiritTemp_html'):
        tag.string.replace_with(SmartSwitch.read_set_temp())

    # Zmiana html aktualnej i zadanej temperatury oleju
    SmartSwitch.switch_to_channel_c()
    for tag in soup.find_all(id='CurrentOilTemp_html'):
        tag.string.replace_with(SmartSwitch.read_current_temp())
    for tag in soup.find_all(id='SetOilTemp_html'):
        tag.string.replace_with(SmartSwitch.read_set_temp())

    # Zmiana html aktualnej i zadanej temperatury soli
    SmartSwitch.switch_to_channel_d()
    for tag in soup.find_all(id='CurrentSaltTemp_html'):
        tag.string.replace_with(SmartSwitch.read_current_temp())
    for tag in soup.find_all(id='SetSaltTemp_html'):
        tag.string.replace_with(SmartSwitch.read_set_temp())

    # Odczyt i zmiana IDN Mostka 1
    for tag in soup.find_all(id="Mostek1Idn_html"):
        tag.string.replace_with(str(SuperTermo.read_idn()+" "+ SuperTermo.port))
        
    # Odczyt i zmiana Read Temp Mostka 1
    for tag in soup.find_all(id="Mostek1Odczyt_html"):
        tag.string.replace_with(SuperTermo.read_current_temp())

    # Obsługa i aktualizacja pliku HTML
    new_html = soup.prettify()
    html_file = open(path, mode='w', encoding='utf-8')
    try:
        html_file.write(new_html)
    except IOError:
        print("HTMLWrite Error")
    else:
        print(str("HTML write OK at: " + dataString))
    html_file.close()

    time.sleep(1)
    
# TODO:
# Dodać html z logiem do /log.html                                  [ ]
# Do obiektu soup wczytywać plik 'wzorcowy' a nie ten z serwera     [ ]
# Zapisywać dane z termostatów do json'a                            [ ]
# Dane z mostków - gdzie i jakie                                    [ ]
# Możliwość ustawienia zdalnego temperatury (okno kto wprowadza t.  [ ]

# TODO v2
#                       PYTHON
# Dane z termostatow wrzucac do jsona                               [ ]
# Uaktualnic biblloteke SmartSwich o mozliwosc wyslania do termos.  [ ]
# Pobieranie danych z json2 + akcja (nastaw term, +ustawienia)      [ ]
# Mostki ??? - chyba nie

#                   Strona WWW - Angular + Material:
# Automatyczna aktualizacja temperatury temp z jsona                [ ]
# Zapis danych od klienta do jsona2                                 [ ]
# Możliwość ustawienia żądanej temp na konkretnym termostacie       [ ]
# Potwierdzenie ustawienia temp - nazwisko, kto ustawil (popup)     [ ]
# Możliwosc zaplanowania o ktorej godz wystartuje term z nastawa    [ ]
# 


