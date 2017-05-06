from pygame import mixer
from time import sleep
from os import listdir, getcwd
from speech_test import listen


class Song(object):
    def choose_song(self):
        self.currentdir = getcwd()
        for file in listdir(self.currentdir):
            if file.endswith(".mp3"):
                print(file)

        self.choice = listen()
        self.choice = self.choice[:1].upper() + self.choice[1:]
        return self.choice + ".mp3"
        

    def play_song(self):
        self.path = self.choice + ".mp3"
        self.path = "songs/" + self.path
        mixer.init()
        mixer.music.load(self.path)
        mixer.music.set_volume(0.0)
        mixer.music.play()

    def increasing_volume(self):
        # mixer.music.set_volume(0.0)
        self.is_max = False

        self.volume = [x / 10 for x in range(1, 11)]
        for i in range(len(self.volume)):
            mixer.music.set_volume(self.volume[i])
            sleep(5)

        if mixer.music.get_volume() == 1.0:
            self.is_max = True

    def pause(self):
        mixer.music.pause()

    def stop(self):
        mixer.music.stop()

    def check(self):
        print(mixer.music.get_busy())

    def check_volume(self):
        print(mixer.music.get_volume())
