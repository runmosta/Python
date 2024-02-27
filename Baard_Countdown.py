import tkinter as tk
from datetime import datetime, timedelta
import winsound  # For platform-specific sound playback

def update_countdown():
    """Updates the countdown display and triggers actions upon completion."""
    global target_time, running, alarm_sound

    # ... (rest of the update_countdown function)

def start_countdown():
    """Starts the countdown."""
    global target_time, running

    # ... (rest of the start_countdown function)

def pause_countdown():
    """Pauses the countdown."""
    global running

    # ... (rest of the pause_countdown function)

def reset_countdown():
    """Resets the countdown to the default or selected time."""
    global target_time, running

    # ... (rest of the reset_countdown function)

def set_alarm():
    """Prompts the user to select an alarm sound file."""
    global alarm_sound

    # ... (rest of the set_alarm function)

def set_default_time():
    """Sets the default countdown time to 1:30."""
    global time_options

    # ... (rest of the set_default_time function)

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Countdown label
countdown_label = tk.Label(root, font=("Arial", 40), text="01:30:00")
countdown_label.pack(pady=20)

# Time options dropdown menu
time_options = tk.StringVar()
time_options.set("01:30")  # Set default option
time_options_menu = tk.OptionMenu(root, time_options, "00:15", "00:30", "01:00", "01:30", command=lambda _: update_countdown())
time_options_menu.pack()

# Start button
start_button = tk.Button(root, text="Start", command=start_countdown, state=tk.NORMAL)
start_button.pack(side=tk.LEFT, padx=10)

# Pause button
pause_button = tk.Button(root, text="Pause", command=pause_countdown, state=tk.DISABLED)
pause_button.pack(side=tk.LEFT, padx=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_countdown, state=tk.NORMAL)
reset_button.pack(side=tk.LEFT, padx=10)

# Rest of the code, including:

# Set alarm button
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(side=tk.LEFT, padx=10)

# ... any other remaining functions and widgets

# Start the main loop
root.mainloop()
