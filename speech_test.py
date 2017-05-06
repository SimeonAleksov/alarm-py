#!/usr/bin/env python3

import speech_recognition as sr
from speech_api import WIT_AI_KEY
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 150)

engine.say("Welcome, please choose song ")
engine.runAndWait()


def listen():
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
