import tkinter as tk
from datetime import timedelta

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        # Default countdown time (1 hour and 30 minutes)
        self.default_time = timedelta(minutes=90)
        self.remaining_time = self.default_time
        self.paused = False

        # Create labels to display time
        self.time_label = tk.Label(master, font=("Helvetica", 24))
        self.time_label.pack()

        # Buttons
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer)
        self.pause_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack()

        # Set initial display
        self.update_display()

    def update_display(self):
        if not self.paused:
            self.remaining_time -= timedelta(seconds=1)
        minutes, seconds = divmod(self.remaining_time.seconds, 60)
        self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
        self.master.after(1000, self.update_display)

    def start_timer(self):
        self.paused = False

    def pause_timer(self):
        self.paused = True

    def stop_timer(self):
        self.remaining_time = self.default_time
        self.paused = True
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = CountdownTimer(root)
    root.mainloop()
