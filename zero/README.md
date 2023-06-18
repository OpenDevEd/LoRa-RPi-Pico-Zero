Code for Raspberry Pi Zero

Use raspberry pi imager to flash an SD card

In imager advanced options before writing image, set username and password

Use PuTTy to set SSH connection. Find IP of rpi using ping -a to set hostname in imager and ping -f hostname

Using this SSH connection, enable VNC server by logging into rpi and using rasp config

https://raspberrytips.com/use-vnc-raspberry-pi/

Once successful, run sudo apt upgrade and update


To work with rfm9x module in rpi zero

install libraries of cicrcuit python first

https://learn.adafruit.com/adafruit-radio-bonnets/rfm9x-raspberry-pi-setup

Enable SPI in rasp-pi config in interface options