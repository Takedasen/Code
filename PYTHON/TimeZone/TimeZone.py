import datetime
import pytz
import tkinter as tk
from tkinter import ttk


class TimeZone:
    def __init__(self, master):
        self.master = master
        self.master.title("TimeZone")

        #! Create a style for the GUI
        style = ttk.Style()
        style.configure(
            "TLabel",
            font=("Calibri", 20),
            padding=20,
            foreground="red",
            background="black",
        )
        style.configure(
            "TButton",
            font=("Calibri", 20),
            padding=20,
            foreground="red",
            background="black",
        )

        #! Create a dropdown menu with popular timezones
        popular_timezones = [
            "US/Pacific",
            "US/Mountain",
            "US/Central",
            "US/Eastern",
            "Europe/London",
            "Europe/Paris",
            "Europe/Kyiv",
            "Asia/Calcutta",
            "Asia/Hong_Kong",
            "Asia/Tokyo",
            "Australia/Sydney",
        ]
        self.timezone_var = tk.StringVar()
        self.timezone_var.set("UTC")
        timezone_label = ttk.Label(
            self.master, text="Timezone Selection :", style="TLabel"
        )
        timezone_label.grid(row=0, column=0, padx=20, pady=20)
        timezone_menu = ttk.OptionMenu(
            self.master, self.timezone_var, *popular_timezones
        )
        timezone_menu.grid(row=0, column=1, padx=20, pady=20)

        #! Create a label to display the current time in the selected timezone
        self.time_var = tk.StringVar()
        time_label = ttk.Label(self.master, textvariable=self.time_var, style="TLabel")
        time_label.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        #! Create a button to update the displayed time
        update_button = ttk.Button(
            self.master, text="GO", command=self.update_time, style="TButton"
        )
        update_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        #! Set the initial time display
        self.update_time()

    def update_time(self):
        #! Get the current time in UTC
        utc_now = datetime.datetime.utcnow()

        #! Convert to the selected timezone
        tz = pytz.timezone(self.timezone_var.get())
        local_now = utc_now.replace(tzinfo=pytz.utc).astimezone(tz)

        #! Update the displayed time
        self.time_var.set(local_now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))


if __name__ == "__main__":
    root = tk.Tk()
    #! Set the background color of the root window to black
    root.configure(background="black")
    app = TimeZone(root)
    root.mainloop()
