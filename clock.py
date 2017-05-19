# clock.py

from time import sleep
from os import system, listdir, getcwd
from datetime import datetime
from pygame import mixer
from music import Song
from actual_clock import Clock
from threading import Thread
c = Clock()

t2 = Thread(target=c.check_time)
t1 = Thread(target=c.show_clock)
t1.start()
t2.start()
