def setup_alarm():
    """Using this function to get the wake up time"""
    user_input = input("Enter when when you want to wake up (HH : MM): ")
    alarm = [int(time) for time in user_input.split() if time.isdigit()]

    return alarm[0], alarm[1]
