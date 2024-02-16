import tkinter as tk
from tkinter import messagebox
import time
import winsound

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Countdown Clock')
        
        # Create input field for time in the format hour:minute:second
        self.entry_time = tk.Entry(self.master, width=10, justify='center')
        self.entry_time.grid(row=0, column=0, columnspan=3)
        self.entry_time.insert(0, "00:00:00")

        self.timer_label = tk.Label(self.master, text="00:00:00", font=("Helvetica", 48))
        self.timer_label.grid(row=1, column=0, columnspan=3, pady=(10, 0))

        start_button = tk.Button(self.master, text='Start', command=self.start_timer)
        start_button.grid(row=2, column=0, pady=5)

        stop_button = tk.Button(self.master, text='Stop', command=self.stop_timer)
        stop_button.grid(row=2, column=2, pady=5)

        self.running = False

    def start_timer(self):
        if not self.running:
            try:
                # Parse the time input from the user
                time_str = self.entry_time.get()
                hours, minutes, seconds = map(int, time_str.split(":"))
                self.total_time = hours * 3600 + minutes * 60 + seconds
                self.running = True
                self.update_timer()
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Please use the format HH:MM:SS")

    def stop_timer(self):
        # Stop the countdown
        self.running = False

    def update_timer(self):
        if self.total_time <= 0:
            # Play the system "hand" sound
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.running = False
        elif self.running:
            self.total_time -= 1
            time_str = time.strftime('%H:%M:%S', time.gmtime(self.total_time))
            self.timer_label.config(text=time_str)
            # After 1 second, call this function again only if running is True
            self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()