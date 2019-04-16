from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI (v1 - v3B+) as of Jan. 2019
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

i=0
while True:
    lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S\n')
    lcd_line_2 = "PodZero Alpha " + str(i)


    if i < 9:
        i = i +1
    else:
        i = 0

    # combine both lines into one update to the display
    lcd.message = lcd_line_1 + lcd_line_2

    sleep(2)