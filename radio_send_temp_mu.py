# Write your code here :-)
import radio
from microbit import *

radio.on()

while True:
    if button_a.was_pressed():
        radio.send(str(temperature()))
