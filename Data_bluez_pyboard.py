
import bluetooth
import re
bd_addr = "20:16:05:12:05:13" #itade address

port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print('Connected')
sock.settimeout(2.0)

while True:
    sock.send(b'D')
    # data = sock.recv(1)
    # data = data.decode("utf-8")
    # if data != '~':
    dr=""
    while True:
        data = sock.recv(1)
        data=data.decode("utf-8")
        if data =='|' :break
        dr+=data

    print(dr)


sock.close()
#-----------------------------------------------------------------

'''
from bluetooth import *


class Devices:
   def __init__( self, target_device_name):
      self.target_device=target_device_name
      self.target_device_address= None

   def check_devices(self):
      discovered_devices=discover_devices()
      for address in discovered_devices:
        if self.target_device==lookup_name(address):
            self.target_device_address=address
            break

   def device_found(self):
      self.check_devices()
      if self.target_device_address is not None:
         return self.target_device_address
      else:
        return None

user_device= input("Enter the device to bediscovered:")
device = Devices(user_device)
addr = device.device_found()

if addr is not None:
      print ("The address for the device is :",addr)
else:
      print ("The device could not be discovered")

'''