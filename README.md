# MorseCode
Translates typed English into Morse code on the screen or with a blinking LED on a Raspberry Pi.

This is a simple Python script which will take text at the command prompt and translate it into
Morse Code.  The Morse Code is printed to the screen and then sent electronically to a LED connected
to a Raspberry Pi GPIO bus.

In order to use with the LED on the Raspberry Pi, the setup and explanation at this website is helpful:
https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

The code is set up to interact with the LED on GPIO 18.  Another pin can be used but be sure to update
the code in the transmit() funtion.

The Morse Code is stored in MorseCode.json and can be edited there if changes should need to be made.

If the code is run on another system, besides a Raspberry Pi, the GPIO import line may not work.  
Also you should comment out or remove any call to the transmit() function as this is the function
that accesses the GPIO.
