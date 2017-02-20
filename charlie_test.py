import sys
import os
from time import sleep
import glob
import serial
# from transceiver import Transceiver
# from flow_sensor import FlowSensor
# from rain_guage import RainGuage
# from level_sensor import LevelSensor
from time import time


## gpio pins for the sensors 

def detect_rain(xbee,rain_guage, level_sensor):
  while True:
    pool_confirmation = ""
    rain_confirmation = ""
    tmp_level = 0 
    rainfall = 0
    if rain_guage.guage_status():
      tmp_level = level_sensor.get_Level()
      if tmp_level <= 0:
        pool_level = 12
      while pool_confirmation != "stop":
        if  rain_guage.get_rain():
          rainfall += rain_guage.calc_tick()
        pool_confirmation = xbee.receive_message()
        xbee.send_message(str(pool_level)+'\n')

      xbee.clear_serial()
      while rain_guage.guage_status():
        rainfall += rain_guage.get_rain()

      while rain_confirmation != 'stop':
        rain_confirmation = xbee.receive_message()
        xbee.send_message(str(rainfall))

      xbee.clear_serial()

def outfall_detection(flow_sensor,xbee):

  while True:
    outfall_confirmation = ""
    if flow_sensor.get_status():

      while outfall_confirmation != 'stop':
        outfall_confirmation = xbee.receive_message()
        xbee.send_message('out\n')

if __name__ == "__main__":
  # rain_guage = RainGuage()
  # flow_sensor = FlowSensor()
  # level_sensor = LevelSensor()
  ##create rainfall_detection thread
  ## pass the rainfall detection function 
  ##create outfall detection thread
  ## pass the outfall detection thread 
  pass