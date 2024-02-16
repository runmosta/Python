import tkinter as tk
from tkinter import messagebox
import time
import winsound

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Countdown Clock')

        # Create the input field for time in the format of hour:minute:second
        self.entry_time = tk.Entry(self.master, width=10, justify='center')
        self.entry_time.grid(row=0, column=0, columnspan=3)
        self.entry_time.insert(0, "00:15:00")  # Default timer set to 15 minutes for demonstration

        self.timer_label = tk.Label(self.master, text="00:00:00", font=("Helvetica", 48))
        self.timer_label.grid(row=1, column=0, columnspan=3, pady=(10, 0))

        # Step control (optional)
        self.step_enabled = tk.BooleanVar(value=False)  # Step feature is disabled by default
        self.step_checkbox = tk.Checkbutton(self.master, text='Enable step "Add water" 15 min before the end', variable=self.step_enabled)
        self.step_checkbox.grid(row=3, column=0, columnspan=3)
        
        start_button = tk.Button(self.master, text='Start', command=self.start_timer)
        start_button.grid(row=2, column=0, pady=5)

        stop_button = tk.Button(self.master, text='Stop', command=self.stop_timer)
        stop_button.grid(row=2, column=2, pady=5)

        self.running = False
        self.step_triggered = False  # Tracks whether the preparation step has been triggered

        # Define the preparation step. It will trigger 15 minutes (900 seconds) before the total time
        self.prep_step = ("Add water", 900)  # (Message, Time before total in seconds)

    def start_timer(self):
        if not self.running:
            try:
                # Parse the time input from the user
                time_str = self.entry_time.get()
                hours, minutes, seconds = map(int, time_str.split(":"))
                self.total_time = hours * 3600 + minutes * 60 + seconds
                self.running = True
                self.step_triggered = False  # Reset the step trigger
                self.update_timer()
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Please use the format HH:MM:SS")

    def stop_timer(self):
        self.running = False

    def update_timer(self):
        if self.total_time <= 0:
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.running = False
            self.timer_label.config(text="00:00:00")
        elif self.running:
            self.total_time -= 1
            # Check if it's time to trigger the preparation step (only if the option is enabled)
            if self.step_enabled.get() and not self.step_triggered and self.total_time == self.prep_step[1]:
                self.step_triggered = True
                self.display_prep_step()
            time_str = time.strftime('%H:%M:%S', time.gmtime(self.total_time))
            self.timer_label.config(text=time_str)
            self.master.after(1000, self.update_timer)

    def display_prep_step(self):
        # Play a sound to alert the user of the preparation step
        winsound.MessageBeep(winsound.MB_ICONINFORMATION)
        # Show a message box with the preparation step information
        messagebox.showinfo("Preparation Step", self.prep_step[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()