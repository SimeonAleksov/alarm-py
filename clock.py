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
    return choice

 # loading a song to play

def play_song(path):

    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

# attemp to increase volume

#def increase_volume():
#    volume = 0.1
#    mixer.set_volume(volume)
#    while not volume:
#        volume += 0.1
#        sleep(0.5)
#        mixer.set_volume(volume)

def pause():
    mixer.pause()

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
                print("alarm")
            sleep(0.2)
        # stop
        except KeyboardInterrupt:
            clear()


show_clock()
