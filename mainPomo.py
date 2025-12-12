from datetime import datetime
import time

from strudel import *

# Print time start & finish
current_time = datetime.now()
print(current_time)

# Active (on) timer vs break (15) in minutes
# After 4 pomodoros, take a longer break 15-30 minutes
pomOn = int(25 * 60) # Seconds
pomOff = int(15 * 60) # Seconds

def music():
    note("<[c3 e3 g3 b3]>").sound("piano").room(0.8)


def countdown(t):

    while t > 0:
        minutes, remaining_seconds = divmod(t, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, remaining_seconds)

        print(time_format)
        t -= 1 # Countdown #
        time.sleep(1)
    print("Break Time!!")

#function call
#countdown(int(pomOn))
music()