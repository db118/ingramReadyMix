import serial
from transceiver import Transceiver
import glob
import sys

def xbee_usb_port():
  '''
  Search in your file directory to find Usb port 
  that your Xbee is connected to. Supports MacOs and 
  linux operating system. Returns a list of usb ports. 
  '''
  result = []
  if sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/tty.usbserial*')
  elif sys.platform.startswith('linux'):
    ports = glob.glob('/dev/ttyU*')
    
  for port in ports:
      try:
          ser = serial.Serial(port)
          ser.close()
          result.append(port)
      except( OSError, serial.SerialException):
          pass
  return result[0]

def main():
  port = xbee_usb_port()
  xbee = Transceiver(9600,port)
  trigger = ""
  while True:
    for x in range(1000):
      trigger = xbee.receive_message()

    if trigger == "tri":
      print('receive trigger')
      for x in xrange(30):
        xbee.send_message('ctri\n')
      print('sending confirmation')
      break

if __name__ == "__main__":
  main()

