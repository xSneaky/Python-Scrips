#Server resource monitor with URL status check
from psutil._common import bytes2human
import datetime
import requests
import psutil
import xmpp
import time
from datetime import datetime

def Cry():
    jid = xmpp.protocol.JID('USER') #xmpp username to login to
    cl=xmpp.Client(jid.getDomain(),debug=False)
    cl.connect()
    cl.auth(jid.getNode(),"PASS", sasl=1)# xmpp password
    cl.send(xmpp.protocol.Message('receiver',message))#receiver ID

#Pings
midnight_alert = "00:00:00"
afternoon_alert = "12:00:00"

CPU_Limit = 1
RAM_Limit = 536870912

CPU_Counter = 10
RAM_Counter = 10
CPU_RAM_Counter = 10

Check_Webserver = 60
Counter_Reset = 60
session = requests.session()

session.proxies = {'http':  'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'} #comment this if you are not using proxy

URL = "URL" #URL To check

while True:
    Counter_Reset -= 1
    if Counter_Reset == 0:
        RAM_Counter = 10
        CPU_Counter = 10

    CPU = psutil.cpu_percent(interval=1, percpu=False)
    RAM = ram_usage_bytes = psutil.virtual_memory()[3]
    RAM_READABLE = bytes2human(ram_usage_bytes)

    if float(CPU) >= CPU_Limit and float(RAM) >= RAM_Limit:
        CPU_RAM_Counter -= 1
        if CPU_RAM_Counter == 0:
            CPU_RAM_Counter = 10
            Check_Webserver = 60
            try:
                check = session.get(URL)
                if check.status_code != 200:
                    message = "CPU Warning: " + str(CPU) + "%" + "\nRAM Warning: " + str(RAM_READABLE) + "\nWeb Server: " + check.status_code
                    Cry()

                elif check.status_code == 200:
                    message = "CPU Warning: " + str(CPU) + "%" + "\nRAM Warning: " + str(RAM_READABLE) + "\nWeb Server: Online"
                    Cry()
            except requests.exceptions.ConnectionError:
                message = "CPU Warning: " + str(CPU) + "%" + "\nRAM Warning: " + str(RAM_READABLE) + "\nTor Proxy Down"
                Cry()

    elif float(CPU) >= CPU_Limit:
        RAM_Counter -= 1
        if RAM_Counter == 0:
            Check_Webserver = 60
            try:
                check = session.get(URL)
                if check.status_code != 200:
                    message = "CPU Warning: " + str(CPU) + "%" + "\nRAM: " + str(RAM_READABLE) + "\nWeb Server: " + check.status_code
                    Cry()
                else:
                    message = "CPU Warning: " + str(CPU) + "%" + "\nRAM: " + str(RAM_READABLE) + "\nWeb Server: Online"
                    Cry()
            except requests.exceptions.ConnectionError:
                message = "CPU Warning: " + str(CPU) + "%" + "\nRAM: " + str(RAM_READABLE) + "\nWeb Server: " + "\nTor Proxy Down"
                Cry()

    elif float(RAM) >= RAM_Limit:
        RAM_Counter -= 1
        if RAM_Counter == 0:
            Check_Webserver = 60
            try:
                check = session.get(URL)
                if check.status_code != 200:
                    message = "CPU: " + str(CPU) + "%" + "\nRAM Warning: " + str(RAM_READABLE) + "\nWeb Server: " + check.status_code
                    Cry()
                else:
                    message = "CPU: " + str(CPU) + "%" + "\nRAM Warning: " + str(RAM_READABLE) + "\nWeb Server: Online"
                    Cry()
            except requests.exceptions.ConnectionError:
                message = "CPU: " + str(CPU) + "%" + "\nRAM Warning: " + str(RAM_READABLE) + "\nWeb Server: " + "\nTor Proxy Down"
                Cry()

    Check_Webserver -= 1
    print(str(Check_Webserver))
    if Check_Webserver == 0:
        Check_Webserver = 60
        try:
            check = session.get(URL)
            if check.status_code != 200:
                message = "CPU: " + str(CPU) + "%" + "\nRAM: " + str(RAM_READABLE) + "\nWeb Server: " + check.status_code
                Cry()
        except requests.exceptions.ConnectionError:
            message = "CPU: " + str(CPU) + "%" + "\nRAM: " + str(RAM_READABLE) + "\nWeb Server: " + "\nTor Proxy Down"
            Cry()
    
    #i am alive
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
   # print(current_time)
    if current_time == afternoon_alert or midnight_alert:
        message = "Still alive !!"
