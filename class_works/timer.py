import time

hour = 0
while hour < 24:
    minute = 0
    while minute < 60:
        second = 0
        while second < 60:
            time.sleep(0.001)
            print(f'Time Elapsed: {hour:0>2}:{minute:0>2}:{second:0>2}', end = "\r")  # end = "\r"
            second += 1
        minute += 1
    hour += 1
