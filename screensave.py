#!/usr/bin/env python
#screensave.py
import subprocess
import sys
import os
import memcache # sudo apt-get install memcached python-memcache

shared = memcache.Client(['127.0.0.1:11211'], debug=0)

play = shared.get('play')
screensaver = shared.get('screensaver')

if not play:
  play = "0"
  shared.set('play', play)

if not screensaver:
  screensaver = "0"
  shared.set('screensaver', screensaver)

parameters = len(sys.argv)  # number of parameters including call itself
if parameters < 2: 
  print("Error: not enough parameters")
  print("Usage: ")
  print("play: Kodi playing")
  print("stop: Kodi stopped")
  print("ss_act: Kodi screensaver active")
  print("ss_inact: Kodi screensaver inactive")
  print("play " + play + " scr " + screensaver)
  sys.exit()


parameters = len(sys.argv)  # number of parameters including call itself
i = 1
if sys.argv[i] == "play":
  play = "1"
elif sys.argv[i] == "stop" : play = "0"
elif sys.argv[i] == "ss_act" : screensaver = "1"
elif sys.argv[i] == "ss_inact" : screensaver = "0"
else:  
  print("Error: wrong parameters")
  sys.exit()

shared.set('play', play)
shared.set('screensaver', screensaver)


if play == "0" and screensaver == "1":
  subprocess.call(["/opt/vc/bin/vcgencmd", "display_power", "0"])
if play == "1":
  subprocess.call(["/opt/vc/bin/vcgencmd", "display_power", "1"])

print("play " + play + " scr " + screensaver)
