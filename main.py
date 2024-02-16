import tkinter as tk
import time
import winsound

class CountdownApp:
    # ... Previous methods remain unchanged ...

    def update_timer(self):
        if self.total_time <= 0:
            # Play the system "hand" sound
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.running = False
        elif self.running:
            # ... Update time and schedule next call to update_timer ...

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()