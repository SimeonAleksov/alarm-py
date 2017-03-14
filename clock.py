# clock.py

from time import sleep
from os import system, listdir, getcwd
from datetime import datetime
from pygame import mixer


def clear():
    system("clear")

user_input = input("Enter when you want to set up alarm (HH : MM): ")
alarm = [int(time) for time in user_input.split() if time.isdigit()]

hour, minute = alarm[0], alarm[1]

def choose_song():
    current_dir = getcwd()
    for file in listdir(current_dir):
        if file.endswith(".mp3"):
            print(file)
    choice = input("Choose song for the alarm: ")
    return choice + ".mp3"

 # loading a song to play

def play_song(path):

    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

# attemp to increase volume

def increase_volume():
    mixer.music.set_volume(0.0)
    volume = [x/10 for x in range(1, 11)]
    for i in range(len(volume)):
        mixer.music.set_volume(volume[i])
        sleep(5)

def pause():
    mixer.music.pause()

def stop():
    mixer.music.stop()


song_choice = choose_song()

def show_clock():
    # we need update our time no
    while True:
        try:
            current_time = datetime.now()
            clear()
            print ("{} : {} : {}".format(current_time.hour, current_time.minute, current_time.second))
            print("Alarm set up in {} : {} : 0".format(hour, minute))

            if current_time.hour == hour and current_time.minute == minute and current_time.second == 0:
                play_song(song_choice)
                increase_volume()
                print("alarm")
            sleep(0.2)
        # stop
        except KeyboardInterrupt:
            clear()


show_clock()
