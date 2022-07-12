import tkinter as tk
from typing_extensions import IntVar


from datetime_utils import *


class DatetimeModule(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 20)


        self.create_datetime_frame()
        self.refresh_time()


    def create_datetime_frame(self):
        def refresh_time(self):
            self.now_time = formatted_time()
            self.time_label.configure(text=now_time)
            self.time_label.after(1000, refresh_time)

        datetime_frame = tk.Frame(
            self, width=100, height=50
        )
        datetime_frame.grid(row=0, column=0, padx=15, pady=15)

        today = formatted_date()
        now_time = formatted_time()

        date_label = IntVar(
            datetime_frame, text=today, font=("Arial", 15)
        )

        date_label.grid(row=0, column=0, padx=10, pady=5)
        time_label = tk.Label(
            datetime_frame, text=now_time, font=("Arial", 20)
        )

        time_label.grid(row=1, column=0, padx=10, pady=5)
        refresh_time()






