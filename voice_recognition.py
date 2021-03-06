#!/usr/bin/env python3

import speech_recognition as sr
WIT_AI_KEY = "P4KSLHTAGW2R3WRWZO3RLIXOI7YLFM5J"
message = ""
def get_hour():
    global message
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please tell the hour when you want to set up the alarm.")
        audio = r.listen(source)
        try:
            message = r.recognize_wit(audio, WIT_AI_KEY)
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print("Could not request results, {0}".format(e))
        finally:
            return message.lower()


def get_minute():
    global message
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please tell the minute when you want to set up the alarm.")
        audio = r.listen(source)
        try:
            message = r.recognize_wit(audio, WIT_AI_KEY)
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print("Could not request results, {0}".format(e))
        finally:
            return message.lower()

def get_song():
    global message
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please tell the song you want to play.")
        audio = r.listen(source)
        try:
            message = r.recognize_wit(audio, WIT_AI_KEY)
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print("Could not request results, {0}".format(e))
        finally:
            return message.lower()
    
