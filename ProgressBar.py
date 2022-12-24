# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------------------
Title: Classic progress bar interface with tkinter

Remark: This is a custom ProgressBar class implemented using the tkinter module in Python. The ProgressBar class is
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
        """
        This is the constructor of the ProgressBar class. It initializes the Toplevel widget and sets its title,
        dimensions, position, and resizability. It also binds the WM_DELETE_WINDOW protocol to the on_closing method
        and creates the progress bar and label widgets.
        """

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
        """
        This method is called when the user closes the window. It displays a message asking the user to confirm the
        action and either destroys the window or raises it to the top of the window stack based on the user's response.
        """

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
        else:
            self.lift()

    def __update_progress_label__(self) -> str:
        """
        This method returns a string with the current progress of the progress bar, rounded to two decimal places.

        :return: current progress of the progress bar
        """

        value = round(self.__pb['value'], 2)
        return f"Current Progress : {value}%"  # Return a string with the current progress

    def progress(self, *data: float):
        """
        This method takes any number of integer arguments and updates the progress bar with a percentage value
        calculated based on the number of arguments. For example, if the method is called with
        the arguments (10, 5), the progress bar will increase by 50% (10/5 * 100).

        :param data: tuple of numbers with which you divide your process
        """

        percent: float = 0  # Initialize the percent variable to 0
        if data and 0 not in data:  # Check if data is not empty and does not contain 0
            for data in data:  # Calculate the percentage of progress for each value
                if percent == 0:
                    percent = 100 / data
                else:
                    percent /= data

            if self.__pb['value'] < 100:
                self.__pb['value'] += percent
                self.__value_label['text'] = self.__update_progress_label__()

    def get_value(self) -> float:
        """
        This method retrieves the current percentage of the progress bar

        :return: current percentage of the progress bar
        """

        return self.__pb['value']

    def set_value(self, value: float):
        """
        This method initializes the progress bar value. For example if you enter as argument (10) then the
        value of the progressbar will be 10%.

        :param value: the new progressbar percentage
        """

        self.__pb['value'] = value
        self.__value_label['text'] = self.__update_progress_label__()

    def __str__(self) -> str:
        """
        This method displays the returns a string representation of the progress bar, which can be used for debugging
        or for printing the object to the console.

        :return: The tkinter object name and the current progression of the progress bar
        """

        return f"ProgressBar: {super.__str__(self)} | Current progress: {self.__pb['value']}"
