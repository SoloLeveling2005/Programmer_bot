import datetime

def start_time():
    now = datetime.datetime.now()
    now = str(now)
    time_now = now.split(" ")
    time_now = time_now[1].split(".")

    return time_now[0]

