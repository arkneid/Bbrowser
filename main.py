#!/usr/bin/env python3
# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
from res.build_layout import build
from tkinter import *

# Build Window
window = Tk()  # Initialize window
window.title("Bbrowser")
window.geometry("600x600")

# Build layout
build(window)

window.mainloop()  # Maintain window open
