# clock.py

from time import sleep
from os import system
from datetime import datetime
from pygame import mixer


def clear():
    system("clear")

def setup_alarm():
    user_input = input("Enter when you want to set up alarm (HH : MM): ")
    alarm = [time for time in user_input.split() if time.isdigit()]
    return alarm[0], alarm[1]



 # loading a song to play

def play_song(path="Traumer - Hoodlum DESOLAT038.mp3"):

    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

# hour, minute = setup_alarm()

def show_clock():
    hour, minute = setup_alarm()
    # we need update our time no
    while True:
        try:
            print(hour, minute)
            current_time = datetime.now()
            clear()
            print (current_time.hour, ":", current_time.minute, ":", current_time.second)
            # just testing when a time hits certain seconds to print a message

            if current_time.hour == hour and current_time.minute == minute:
                print(hour, minute)
                print ("ITS TIME WAKE UP")
                play_song()
            sleep(0.2)
        # stop
        except KeyboardInterrupt:
            clear()

show_clock()
