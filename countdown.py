import tkinter as tk
from tkinter import messagebox
import time

# Note: Replace winsound with a cross-platform alternative if needed.
import winsound

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Countdown Clock')
        self.master.geometry('500x200')  # Increase the window size for a better layout

        # Timer input field
        self.entry_time = tk.Entry(self.master, width=10, justify='center')
        self.entry_time.grid(row=0, column=1, sticky='w', padx=5, pady=5)
        self.entry_time.insert(0, "01:30:00")  # Default timer set to 90 minutes

        # Primary step time input field
        self.entry_primary_step_time = tk.Entry(self.master, width=5, justify='center')
        self.entry_primary_step_time.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        self.entry_primary_step_time.insert(0, "15")  # Default primary optional step time

        # Secondary step time input field
        self.entry_secondary_step_time = tk.Entry(self.master, width=5, justify='center')
        self.entry_secondary_step_time.grid(row=2, column=1, padx=5, pady=5)
        self.entry_secondary_step_time.insert(0, "30")  # Default secondary optional step time

        # Labels next to input fields
        tk.Label(self.master, text="Enter total time (HH:MM:SS):").grid(row=0, column=0, sticky='e')
        tk.Label(self.master, text="Primary step time (minutes):").grid(row=1, column=0, sticky='e')
        tk.Label(self.master, text="Secondary step time (minutes):").grid(row=2, column=0, sticky='e')

        self.timer_label = tk.Label(self.master, text="01:30:00", font=("Helvetica", 48))
        self.timer_label.grid(row=4, column=0, columnspan=3, pady=(10, 0))

        # Checkboxes to enable optional steps
        self.primary_step_enabled = tk.BooleanVar()
        self.primary_step_checkbox = tk.Checkbutton(self.master, text='Enable primary step', variable=self.primary_step_enabled)
        self.primary_step_checkbox.grid(row=1, column=2, sticky='w')

        self.secondary_step_enabled = tk.BooleanVar()
        self.secondary_step_checkbox = tk.Checkbutton(self.master, text='Enable secondary step', variable=self.secondary_step_enabled)
        self.secondary_step_checkbox.grid(row=2, column=2, sticky='w')

        # Start and Stop buttons
        start_button = tk.Button(self.master, text='Start', command=self.start_timer)
        start_button.grid(row=5, column=0, pady=5)

        stop_button = tk.Button(self.master, text='Stop', command=self.stop_timer)
        stop_button.grid(row=5, column=1, pady=5)

        self.running = False
        self.primary_step_triggered = False
        self.secondary_step_triggered = False

    def start_timer(self):
        try:
            total_time_str = self.entry_time.get()
            primary_step_str = self.entry_primary_step_time.get()
            secondary_step_str = self.entry_secondary_step_time.get()

            hours, minutes, seconds = map(int, total_time_str.split(":"))
            primary_step_minutes = int(primary_step_str)
            secondary_step_minutes = int(secondary_step_str)

            self.total_time = hours * 3600 + minutes * 60 + seconds
            self.primary_step_time = primary_step_minutes * 60
            self.secondary_step_time = secondary_step_minutes * 60
            self.elapsed_time = 0
            self.running = True
            self.primary_step_triggered = False
            self.secondary_step_triggered = False
            self.update_timer()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please use the correct format.")

    def stop_timer(self):
        self.running = False

    def update_timer(self):
        if self.total_time == self.elapsed_time:
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.running = False
            self.timer_label.config(text="00:00:00")
            messagebox.showinfo("Time's Up", "The countdown has finished.")
        elif self.running:
            remaining_time = self.total_time - self.elapsed_time
            # Format the remaining time into "HH:MM:SS"
            time_str = time.strftime('%H:%M:%S', time.gmtime(remaining_time))
            self.timer_label.config(text=time_str)

            # Check for the primary step (if enabled and not yet triggered)
            if self.primary_step_enabled.get() and not self.primary_step_triggered and remaining_time == self.primary_step_time:
                self.primary_step_triggered = True
                self.display_optional_step("Primary Step Alert", "It's time for the primary step!")

            # Check for the secondary step (if enabled and not yet triggered)
            if self.secondary_step_enabled.get() and not self.secondary_step_triggered and remaining_time == self.secondary_step_time:
                self.secondary_step_triggered = True
                self.display_optional_step("Secondary Step Alert", "It's time for the secondary step!")

            self.elapsed_time += 1
            # Schedule the next call to this method after one second
            self.master.after(1000, self.update_timer)

    def display_optional_step(self, title, message):
        winsound.MessageBeep(winsound.MB_ICONHAND)
        messagebox.showinfo(title, message)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()