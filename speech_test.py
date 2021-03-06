#!/usr/bin/env python3

import speech_recognition as sr
WIT_AI_KEY = "JQ2NRHSF5QDBGQJAAJGUHCAAIA7TNSFX"
message = ""
def listen():
    global message
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Welcome, please choose song ")
        audio = r.listen(source)
        try:
            message = r.recognize_wit(audio, WIT_AI_KEY)
            print("You said: " + message)
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print("Could not request results, {0}".format(e))
        finally:
            return message.lower()

listen()
