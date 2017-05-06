# actual_clock.py

from time import sleep
from os import system
from setup_alarm import setup_alarm
from datetime import datetime
from music import Song
from nice_loading import Loading
load = Loading()
s = Song()

song_choice = s.choose_song()


class Clock(object):
    """A class for showing the current time and setting up the alarm"""
    def __str__(self):
        return "Showing the time"


    def __repr__(self):
        return "Digital clock"

    
    def clear(self):
        system("clear")

        
    def get_alarm(self):
        """Getting the hour and minute when you want to wake up"""
        self.hour, self.minute = setup_alarm()
        return self.hour, self.minute

    
    def set_time(self):
        """Returning the time"""
        self.current_time = datetime.now()
        return self.current_time.hour, self.current_time.minute, self.current_time.second
    
    def show_clock(self):
       """Function to show the time"""
       
       hour, minute = self.get_alarm()
       while True:
           try:
               hours, minutes, seconds = self.set_time()
               self.clear()
               print("{} : {} : {}".format(hours, minutes, seconds))
               print("Alarm set up in {} : {} : 0".format(hour, minute))

               if hour == hours and minute == minutes and seconds == 0:
                   load.start()
                   s.play_song()
                   s.increasing_volume()
                   load.stop()

               sleep(0.2)
           except KeyboardInterrupt:
               clear()

