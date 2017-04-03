# clock.py

from time import sleep
from os import system, listdir, getcwd
from datetime import datetime
from pygame import mixer
from music import Song
from actual_clock import Clock

c = Clock()

c.show_clock()
