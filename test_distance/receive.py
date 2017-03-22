import sys
import os
from transceiver import Transceiver
import glob
import serial

def xbee_usb_port():
  if sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/tty.usbserial*')
  elif sys.platform.startswith('linux'):
    ports = glob.glob('/dev/ttyUSB0*')
  if len(ports) != 0:
    result = []
    for port in ports:
        try:
            ser = serial.Serial(port)
            ser.close()
            result.append(port)
        except( OSError, serial.SerialException):
            pass
    return result[0]
  else:
    return None

def send_outfall_conf(xbee):
  message = ""
  while not message == 'out':
    message = xbee.receive_message()
  xbee.send_message("oyes\n")
  print("got the message")
  sleep(0.5)



port = xbee_usb_port()
xbee = Transceiver(9600,port)
while True:
  send_outfall_conf(xbee)