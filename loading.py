from time import sleep
from os import system

def loading():
    system("clear")
    symbols = [".", "..", "..."]
    finished = False
    count = 0
    while not finished:
        for w in symbols:
            print("\r Loading" + w, end='')
            sleep(1)
        count += 1
        system("clear")
        if count == 3:
            finished = True
loading()
print("\n")
