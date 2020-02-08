# MorseCode
Translates typed English into Morse code on the screen or with a blinking LED on a Raspberry Pi.

This is a simple Python script which will take text at the command prompt and translate it into
Morse Code.  The Morse Code is printed to the screen and then sent electronically to a LED connected
to a Raspberry Pi GPIO bus.  The setup for the GPIO is available at (Enter website here.) 

The Morse Code is stored in MorseCode.json and can be edited there if changes should need to be made.

If the code is run on another system, besides a Raspberry Pi, the GPIO import line may not work.  
Also you should comment out or remove the code to send the output to the GPIO.
