from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import RPi.GPIO as GPIO 

# Specify LCD
lcd_columns = 16
lcd_rows = 2

# Setup LCD IO
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D5)
lcd_d7 = digitalio.DigitalInOut(board.D11)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)
# wipe LCD screen before we start
lcd.clear()

# Setup button IO
btn_1 = digitalio.DigitalInOut(board.D17)
btn_1.direction = digitalio.Direction.INPUT
btn_1.pull = digitalio.Pull.DOWN

# Setup temperature sensor, see install.txt for additional information
temperature_dir = "/sys/bus/w1/devices/28-0215c2445fff/w1_slave"

def get_temperature():
  with open(temperature_dir) as f:
    temperature_milli_c = f.read().split("t=")[1].strip()
    temperature_c = int(temperature_milli_c)/1000
    return  temperature_c

while True:
    
    #Button stuff
    if btn_1.value:
       print("button pressed")

    # LCD stuff
    lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S\n')
    lcd_line_2 = get_temperature()

    # combine both lines into one update to the display
    lcd.message = lcd_line_1 + str(lcd_line_2) + ' C'

    sleep(0.01)
