# clock.py

from time import sleep
from os import system
from datetime import datetime
from pygame import mixer


def clear():
    system("clear")

 #loading a song to play

def play_song(path="Traumer - Hoodlum DESOLAT038.mp3"):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

def show_clock():
    #we need update our time no
    while True:
        try:
            current_time = datetime.now()
            clear()
            print current_time.hour, ":",current_time.minute,":",current_time.second
            # just testing when a time hits certain seconds to print a message
            if current_time.second == 5:
                print "ITS TIME WAKE UP"
                play_song()
            sleep(0.2)
        #stop
        except KeyboardInterrupt:
            clear()

show_clock()
