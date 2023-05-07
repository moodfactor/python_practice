import time
import sys


def pomodoro():
    """A Pomodoro timer."""

    # Get the work time from the user.
    work_time = input("Enter the work time in minutes: ")
    work_time = int(work_time)

    # Get the short break time from the user.
    short_break_time = input("Enter the short break time in minutes: ")
    short_break_time = int(short_break_time)

    # Get the long break time from the user.
    long_break_time = input("Enter the long break time in minutes: ")
    long_break_time = int(long_break_time)

    # Initialize the variables.
    work_count = 0
    long_break_count = 0

    # Start the timer.
    while True:
        # Work for the specified amount of time.
        time.sleep(work_time * 60)
        print("Work time is over.")

        # Take a short break.
        time.sleep(short_break_time * 60)
        print("Short break is over.")

        # Increase the work count.
        work_count += 1

        # If the work count is a multiple of four, take a long break.
        if work_count % 4 == 0:
            time.sleep(long_break_time * 60)
            print("Long break is over.")
            long_break_count += 1

        # If the long break count is four, reset the work count and long break count.
        if long_break_count == 4:
            work_count = 0
            long_break_count = 0


if __name__ == "__main__":
    # Call the pomodoro() function.
    pomodoro()
