'''
Rishabh Panda
1904215 (ETC3)

KIIT University, Bhubaneswar
'''

import speech_recognition as sr
import pyttsx3

# Initializing the recognizer
recognizer = sr.Recognizer()

# Function for text to speech conversion
def Text2Speech(command):
    # Initializing the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Handling exceptions at the runtime
try:

    # using microphone as input source.
    with sr.Microphone() as source2:

        # Adjusting the energy threshold based on the surrounding noise level
        print("Calibrating background noise...")
        recognizer.adjust_for_ambient_noise(source2, duration=0.2)
        print("Calibration successful. Prescribe!")

        # listening user's input
        audio2 = recognizer.listen(source2)

        # Using Google Web Speech API to recognize audio
        MyText = recognizer.recognize_google(audio2)
        MyText = MyText.lower()

        # Confirmation using text and audio
        print(MyText)
        Text2Speech(MyText)

except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

except sr.UnknownValueError:
    print("unknown error occurred")
