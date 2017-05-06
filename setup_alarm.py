from speech_test import listen
from times import oclock

def get_message():
    message = listen()
    return message
    
def setup_alarm():
    """Using this function to get the wake up time"""
    user_input = input("Say when when you want to wake up (HH : MM): ")
    # msg = get_message()
    # if msg in oclock:
    #    print(oclock[msg])
    #    return int(oclock[msg])
    alarm = [int(time) for time in user_input.split() if time.isdigit()]
    return alarm[0], alarm[1]
