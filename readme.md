

lg-control.py
With this script you can control your LG tv from a raspberry PI. The original script can be found https://harizanov.com/2013/12/control-lg-smart-tv-over-the-internet-using-a-raspberry-pi/ and https://github.com/ubaransel/lgcommander.

Somehow searching the TV didn't work for me so I've made the IP fixed. You should change this to your tv's IP in line 16 lgtv["ipaddress"] = "192.168.1.111". 
If you want to enable searching, uncomment line 85 #lgtv["ipaddress"] = getip()
After first connection the TV will show a pairing key. Change this in line 15 lgtv["pairingKey"] = "724855"

I've also added support for multiple commands from the command line, separated by spaces. The script will send them to the TV with 0.1 sec delay in between.