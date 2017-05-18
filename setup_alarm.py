from voice_recognition import get_hour, get_minute
from times import clock

def __set_hour():
    hour = get_hour()
    if hour == '':
        hour = 00
        return hour 
    elif hour in clock.keys():
        return clock[hour]
    elif hour not in clock.keys():
        print("Couldn't understand")

def __set_minute():
    minute = get_minute()
    if minute == '':
        minute = 00
        return minute
    elif minute in clock.keys():
        return clock[minute]
    elif minute not in clock.keys():
        print("Couldn't understand")

        
def setup_alarm():
    """Using this function to get the wake up time"""
    __hour = __set_hour()
    __minute = __set_minute()
    
    return __hour, __minute

