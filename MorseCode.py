"""Translates text to Morse Code."""
import json
import RPi.GPIO as GPIO
import time, sys, signal

#constants
MorseJsonFilename = 'MorseCode.json'
letterGap = '   '
wordGap = '       '
endOfMessage = 'EOT'
startingSignal = 'STARTING_SIGNAL'
unrecognizedCharacter = 'ERROR'
timeUnit = 0.15

#signal handler
def end_transmission(signal, frame):
    print('\nTransmission terminated.')
    GPIO.output(18, False)
    GPIO.cleanup()
    sys.exit()
    
#global variables
dictionary = {}


#Get the dictionary
with open(MorseJsonFilename, 'r') as file:
    dictionary = json.load(file)

#Conversion Function
def convert_word(word):
    """Converts a word into Morse Code and appends a space at the end of the 
    word."""
    wordInMorseCode = []
    #Convert the text to all caps
    allCaps = word.upper()
    #Split the text into characters
    letters = list(allCaps)
    #Convert each character to morsecode
    for letter in letters:
        try:
            wordInMorseCode.append(dictionary[letter])
        except KeyError:
            wordInMorseCode.append(dictionary[unrecognizedCharacter])

    #wordInMorseCode.append(' ')
    return wordInMorseCode

def build_message(messageString):
    #break up the message into words
    words = messageString.split()
    #translate words into Morse Code
    mcWords = []
    for word in words:
        mcWords.append(convert_word(word))
    outputString = ''
    for wordIndex, mcWord in enumerate (mcWords):
        for letterIndex, letter in enumerate (mcWord):
            outputString += letter
            if letterIndex != len(mcWord) -1:
                outputString += letterGap
        if wordIndex != len(mcWords) -1:
            outputString +=wordGap
    return outputString

#function to transmit the message on a Raspberry Pi (See Readme)
def transmit (message):
    #Setup the GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    
    try:
        time.sleep(1)
        for char in message:
            if char == '.':
                GPIO.output(18, True)
                time.sleep(timeUnit)
                GPIO.output(18, False)
                time.sleep(timeUnit)
            elif char == '_':
                GPIO.output(18, True)
                time.sleep(timeUnit * 3)
                GPIO.output(18, False)
                time.sleep(timeUnit)
            elif char == ' ':
                time.sleep(timeUnit)
            else:
                print('Unexpected character in the transmit message.')
                break
    except KeyboardInterrupt:
        GPIO.output(18, False)
        GPIO.cleanup()

#start the signal handler
signal.signal(signal.SIGINT, end_transmission)

#Get some text
textToTranslate = input('Please enter some text to translate into Morse Code:\n')
#And build the message
messageToTransmit = build_message(textToTranslate)

#transmit the message
#if it is an emergency, repeat SOS
if textToTranslate == '911' or textToTranslate.upper() == 'SOS':
    messageToTransmit = build_message('SOS')
    print('Transmitting the emergency signal.  Press Ctrl+C to discontinue.')
    while True:
        print(messageToTransmit)
        transmit(messageToTransmit)
else:
    #print the morse code
    print(messageToTransmit)
    transmit(messageToTransmit)

#TODO:  OUTPUT HERE IS ONLY FOR TESTING, REMOVE WHEN DONE TESTING
#################################################################

#################################################################
