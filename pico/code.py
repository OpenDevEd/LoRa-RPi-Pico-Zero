print("Hello World on Pico!")

# print(dir(board))  # List pins
# help(modules)  # List modules

# Simple example to send a message and then wait indefinitely for messages
# to be received.  This uses the default RadioHead compatible GFSK_Rb250_Fd250
# modulation and packet format for the radio.
import board
import busio
import digitalio

import adafruit_rfm9x

import time

# set the time interval (seconds) for sending packets
transmit_interval = 10

# Define radio parameters.
RADIO_FREQ_MHZ = 433.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
CS = digitalio.DigitalInOut(board.GP17)
RESET = digitalio.DigitalInOut(board.GP22)
# Or uncomment and instead use these if using a Feather M0 RFM69 board
# and the appropriate CircuitPython build:
# CS = digitalio.DigitalInOut(board.RFM69_CS)
# RESET = digitalio.DigitalInOut(board.RFM69_RST)

# Define the onboard LED
LED = digitalio.DigitalInOut(board.GP25)
LED.direction = digitalio.Direction.OUTPUT

# Initialize SPI bus, busio.SPI(SCK, MOSI, MISO)
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP16)

# Initialze RFM radio
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# set node addresses
rfm9x.node = 1
rfm9x.destination = 2
# initialize counter
counter = 0
# send a broadcast message from my_node with ID = counter
rfm9x.send(
    bytes("Startup message {} from node {}".format(counter, rfm9x.node), "UTF-8")
)

# Wait to receive packets.
print("Waiting for packets...")
now = time.monotonic()
while True:
    # Look for a new packet: only accept if addresses to my_node
    packet = rfm9x.receive(with_header=True)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header):", [hex(x) for x in packet[0:4]])
        print("Received (raw payload): {0}".format(packet[4:]))
        print("Received RSSI: {0}".format(rfm9x.last_rssi))
    if time.monotonic() - now > transmit_interval:
        now = time.monotonic()
        counter = counter + 1
        # send a  mesage to destination_node from my_node
        rfm9x.send(
            bytes(
                "message number {} from node {}".format(counter, rfm9x.node), "UTF-8"
            ),
            keep_listening=True,
        )
        button_pressed = None