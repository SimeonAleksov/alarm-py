# nice_loading.py

import sys
import time
import threading

class Loading(object):
    busy = False
    delay = 0.1
    
    @staticmethod
    def loading_cursor():
        while True:
            for cur in "|/-\\": yield cur

    def __init__(self, delay=None):
        self.loading_gen = self.loading_cursor()
        if delay and float(delay): self.delay = delay

    def load_task(self):
        while self.busy:
            sys.stdout.write(next(self.loading_gen))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write("\b")
            sys.stdout.flush()

    def start(self):
        self.busy = True
        threading.Thread(target=self.load_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)
            

