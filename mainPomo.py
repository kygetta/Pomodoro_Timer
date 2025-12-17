from datetime import datetime
import time

# Print time start & finish
current_time = datetime.now()
print(current_time)

# Active (on) timer vs break (15) in minutes
# After 4 pomodoros, take a longer break 15-30 minutes

#pomOn = int(25 * 60) # Seconds
#pomOff = int(15 * 60) # Seconds

class Pomodoro:
    def __init__(self):
        self.break_time = int(5) # seconds
        self.work_time = int(10) # seconds
        self.pom_done = 0

    def PomWork(self):
        while self.pom_done < 2:

            # WORK TIME
            print("\n POMODORO START!!")
            self.timer_logic(self.work_time)

            #Increment state counter
            self.pom_done += 1

            if self.pom_done == 2:
                # Work Complete
                print("\n Well Done! The work is complete!")
                break

            # BREAK TIME
            print("\n Break time!")

            print("\n Enjoy the break.. you deserve it!")
            self.timer_logic(self.break_time)

    def PomBreak(self):
        while self.work_time >= 0:
            pomo.timer_logic(self.work_time)
            if self.work_time == 0:

                # Break's up, back to work
                print("\n Time to get back to work. You've got this!")

            timer -= 1

    def timer_logic(self, t):
        while t > 0:
            minutes, remaining_seconds = divmod(t, 60)
            time_format = '{:02d}:{:02d}'.format(minutes, remaining_seconds)
            print(time_format)
            t -= 1 # Countdown #
            time.sleep(1)

#function call
if __name__ == '__main__':
    pomo = Pomodoro()
    pomo.PomWork()