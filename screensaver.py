import tkinter as tk
import time

class Screensaver:
    def __init__(self):
        self.root = tk.Tk()
        
        # Make it fullscreen and remove all window borders/taskbar
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')
        self.root.config(cursor="none") # Hide the mouse cursor

        # Create the Time Label
        self.time_label = tk.Label(
            self.root, text="", font=("Courier", 40), 
            fg="white", bg="black"
        )
        self.time_label.place(relx=0.5, rely=0.45, anchor="center")

        # Create the Bar Label
        self.bar_label = tk.Label(
            self.root, text="", font=("Courier", 20), 
            fg="white", bg="black"
        )
        self.bar_label.place(relx=0.5, rely=0.55, anchor="center")

        # Bind any key or mouse movement to close the screensaver
        self.root.bind("<Any-KeyPress>", lambda e: self.root.destroy())
        self.root.bind("<Motion>", lambda e: self.root.destroy())

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.localtime()
        # 12h format
        time_str = time.strftime("%I:%M:%S %p", now)
        seconds = now.tm_sec

        # Logic for 60-character block bar
        # Using █ (Solid) and ░ (Light shade)
        bar_length = 60
        bar = "█" * seconds + "░" * (bar_length - seconds)

        self.time_label.config(text=time_str)
        self.bar_label.config(text=bar)

        # Update every 100ms
        self.root.after(100, self.update_clock)

if __name__ == "__main__":
    Screensaver()