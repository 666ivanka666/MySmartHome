from doctest import master
import tkinter as tk
from tkinter.colorchooser import askcolor
from turtle import color


class SettingsModule(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 20)

        self.create_test_label()
    
    def create_test_label(self):
        self.test_label = tk.Label(self, text="Settings", font=self.font)
        self.test_label.grid(row=0, column=0)




class SettingsColour(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 20)

       
        self.change_color()


    def change_color(self):
        self.colors = tk.Checkbutton(askcolor(text='Select a Color',font=self.font, command=self.change_color))
        self.configure(bg=self.colors[1])
       

        



