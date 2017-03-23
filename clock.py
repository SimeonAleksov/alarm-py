# clock.py

from time import sleep
from os import system, listdir, getcwd
from datetime import datetime
from pygame import mixer
from music import Song

def clear():
    system("clear")

user_input = input("Enter when you want to set up alarm (HH : MM): ")
alarm = [int(time) for time in user_input.split() if time.isdigit()]

hour, minute = alarm[0], alarm[1]

s = Song()

song_choice = s.choose_song()

def show_clock():
    # we need update our time no
    while True:
        try:
            current_time = datetime.now()
            clear()
            print ("{} : {} : {}".format(current_time.hour, current_time.minute, current_time.second))
            print("Alarm set up in {} : {} : 0".format(hour, minute))

            if current_time.hour == hour and current_time.minute == minute and current_time.second == 0:
                s.play_song()
                s.increasing_volume()
                print("alarm")
            sleep(0.2)
        # stop
        except KeyboardInterrupt:
            clear()


show_clock()
