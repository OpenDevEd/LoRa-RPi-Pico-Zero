# LoRa Raspberry Pi Pico-Zero

Basic test for getting data exchanged between Pico ('node') and Zero ('base station').

1. Generate random number on Pico. Pico sends the number together with date stamp.
2. Zero receives and stores data, and sends acknowledgement.

Pico needs to use `circuipython`. Zero can use anything.

Project ultimately to be integrated with https://github.com/bablokb/pcb-pico-datalogger. The datalogging component reads sensor data and then transmits this to base station.
