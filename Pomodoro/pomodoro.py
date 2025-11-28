import sys
import time


class Pomodoro:
    def __init__(self):
        self._minutes = 25
        self._pomodoros = None

    def set_minutes(self, minutes):
        self._minutes = minutes

    def get_minute(self):
        return self._minutes

    def set_pomodoros(self, intervals):
        self._pomodoros = intervals

    def get_pomodoros(self):
        return self._pomodoros

    def timer(self):
        """ Setting up how long start countdown if not default, pause, skip/finish """
        seconds = self.get_minute() * 60
        for remaining in range(seconds, -1, -1):
            mins, secs = divmod(remaining, 60)
            sys.stdout.write(f"\r{mins:02d} {secs:02d}")
            sys.stdout.flush()
            time.sleep(1)
        print("Time is up")

    """ 
        Managing Logic here, Instead in core/service.py
        TaskService class only calls Pomodoro.main() function 
    """

    def main(self):
        print("Press Ctrl+C anytime to stop the timer.")
        try:
            self.timer()
        except KeyboardInterrupt:
            print("\nTimer stopped early")
            return
