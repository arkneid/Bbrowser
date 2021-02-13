# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
from tkinter import *


def build(window):
    # Button Config
    back_btn = Button(window, text="Back")
    forward_btn = Button(window, text="Forward")

    back_btn.grid(row=0, column=0, sticky="nsew")
    forward_btn.grid(row=0, column=1, sticky="nsew")

    # Text Box
    url_box = Entry(window)
    url_box.grid(row=0, column=3, sticky="nsew")
    Grid.columnconfigure(window, index=3, weight=1)

    # Sub window with scroll
    scroll = Canvas(window, bg="black")
    scroll.grid(row=1, columnspan=4, sticky="nsew")
    Grid.rowconfigure(window, index=1, weight=1)
