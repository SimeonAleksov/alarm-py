# clock.py

from time import sleep
from os import system
from datetime import datetime

def clear():
    system("clear")

def show_clock():
    #we need update our time no
    while True:
        try:
            current_time = datetime.now()
            clear()
            print current_time.hour, ":",current_time.minute,":",current_time.second
            # just testing when a time hits certain seconds to print a message
            if current_time.second == 40:
                print "ITS TIME WAKE UP"
            sleep(0.2)
        #stop
        except KeyboardInterrupt:
            clear()

show_clock()
