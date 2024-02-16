import tkinter as tk
from tkinter import messagebox
import time
import winsound

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Countdown Clock')
        self.master.geometry('400x250')

        # Timer input field
        self.entry_time = tk.Entry(self.master, width=10, justify='center')
        self.entry_time.grid(row=0, column=1, pady=5)
        self.entry_time.insert(0, "01:30:00")  # Default timer set to 90 minutes

        # Step time input field
        self.entry_step_time = tk.Entry(self.master, width=5, justify='center')
        self.entry_step_time.grid(row=1, column=1, pady=5)
        self.entry_step_time.insert(0, "15")  # Default optional step time set to 15 minutes before the end
        
        tk.Label(self.master, text="Enter total time (HH:MM:SS):").grid(row=0, column=0)
        tk.Label(self.master, text="Optional step time (minutes):").grid(row=1, column=0)

        self.timer_label = tk.Label(self.master, text="01:30:00", font=("Helvetica", 48))
        self.timer_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        # Checkbox to enable the optional step
        self.step_enabled = tk.BooleanVar(value=False)
        self.step_checkbox = tk.Checkbutton(self.master, text='Enable optional step', variable=self.step_enabled)
        self.step_checkbox.grid(row=2, column=0, columnspan=2)

        start_button = tk.Button(self.master, text='Start', command=self.start_timer)
        start_button.grid(row=4, column=0)

        stop_button = tk.Button(self.master, text='Stop', command=self.stop_timer)
        stop_button.grid(row=4, column=1)

        self.running = False
        self.step_triggered = False

    def start_timer(self):
        try:
            total_time_str = self.entry_time.get()
            step_time_str = self.entry_step_time.get()
            
            # Parse the total time and the step time input from the user
            hours, minutes, seconds = map(int, total_time_str.split(":"))
            step_minutes = int(step_time_str)
            
            self.total_time = hours * 3600 + minutes * 60 + seconds
            self.optional_step_time = step_minutes * 60  # Convert minutes to seconds
            self.elapsed_time = 0
            self.running = True
            self.step_triggered = False
            self.update_timer()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please use the correct format.")

    def stop_timer(self):
        self.running = False

    def update_timer(self):
        if self.total_time == self.elapsed_time:
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.running = False
            messagebox.showinfo("Time's Up", "The countdown has finished.")
            self.timer_label.config(text="00:00:00")
        elif self.running:
            remaining_time = self.total_time - self.elapsed_time
            time_str = time.strftime('%H:%M:%S', time.gmtime(remaining_time))
            self.timer_label.config(text=time_str)
            self.elapsed_time += 1

            if self.step_enabled.get() and not self.step_triggered and remaining_time == self.optional_step_time:
                self.step_triggered = True
                self.display_optional_step()

            self.master.after(1000, self.update_timer)

    def display_optional_step(self):
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
        messagebox.showinfo("Preparation Step", "It's time for the optional step!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()