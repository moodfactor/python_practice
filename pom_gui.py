import tkinter as tk
import time

# Define global constants
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60

# Set up the UI
window = tk.Tk()
window.title("Pomodoro Timer")

# Create the countdown label
countdown_label = tk.Label(text="25:00")
countdown_label.pack()

# Create the start button
start_button = tk.Button(text="Start", command=start_timer)
start_button.pack()

# Create the reset button
reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.pack()

# Create the sound player
sound_player = tk.Sound("bell.wav")


# Define the start_timer function
def start_timer():
    # Start the countdown
    countdown = WORK_TIME
    while countdown > 0:
        # Update the countdown label
        countdown_label.config(text="%02d:%02d" % (countdown // 60, countdown % 60))
        # Sleep for 1 second
        time.sleep(1)
        countdown -= 1

    # Play a sound when the timer is finished
    sound_player.play()

    # Check if it's time for a short break or a long break
    if countdown == 0:
        if work_count % 4 == 0:
            # It's time for a long break
            work_count = 0
            short_break_count = 0
            countdown = LONG_BREAK_TIME
        else:
            # It's time for a short break
            short_break_count += 1
            countdown = SHORT_BREAK_TIME

    # Start the countdown again
    start_timer()


# Define the reset_timer function
def reset_timer():
    # Reset the countdown label
    countdown_label.config(text="25:00")
    # Reset the work count
    work_count = 0
    # Reset the short break count
    short_break_count = 0


# Start the timer
start_timer()

# Keep the window open until the user closes it
window.mainloop()
