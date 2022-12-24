# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------------------
Title: Classic progress bar interface with tkinter

Remark : This is a custom ProgressBar class implemented using the tkinter module in Python. The ProgressBar class is
a top-level window that displays a horizontal progress bar and a label that shows the current progress. The progress
bar can be updated using the progress method, which takes one or more integers as arguments and increases the
progress bar by a percentage of the total progress for each integer. The get_value method returns the current
progress of the progress bar as an integer, and the set_value method allows you to set the progress of the progress
bar to a specific value.

Written by: Jean Guiraud
---------------------------------------------------------------------------------------------------------------
"""
# !/usr/bin/env python3
# Python version : 3.8

from tkinter import messagebox, ttk
from tkinter import *


class ProgressBar(Toplevel):

    def __init__(self):

        super().__init__()

        self.title('Progressbar')

        # get screen width and height
        window_x = self.winfo_rootx()
        window_y = self.winfo_rooty()

        # set the dimensions of the screen
        # and where it is placed
        self.geometry(f'{300}x{120}+{window_x}+{window_y}')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.__on_closing__)

        # self.progressbar
        self.__pb = ttk.Progressbar(
            self,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the self.progressbar
        self.__pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

        # label
        self.__value_label = ttk.Label(self, text=self.__update_progress_label__())
        self.__value_label.grid(column=0, row=1, columnspan=2)

    def __on_closing__(self):
        if messagebox.askokcancel("Quit",
                                  "Do you want to quit? If you stop the progressbar then the generation will stop"):
            self.destroy()
        else:
            self.lift()

    def __update_progress_label__(self):
        value = round(self.__pb['value'], 2)
        return f"Current Progress : {value}%"

    def progress(self, *data: float):

        percent: float = 0
        if data and 0 not in data:
            for data in data:
                if percent == 0:
                    percent = 100 / data
                else:
                    percent /= data

            if self.__pb['value'] < 100:
                self.__pb['value'] += percent
                self.__value_label['text'] = self.__update_progress_label__()

    def get_value(self) -> int:
        return self.__pb['value']

    def set_value(self, value: int):
        self.__pb['value'] = value
        self.__update_progress_label__()

    def __str__(self) -> str:
        return f"Current progress: {self.__pb['value']}"