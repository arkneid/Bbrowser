# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
from gi.repository import Gtk


def search(widget):
    print("cenas")


def build(window):
    grid = Gtk.Grid()
    window.add(grid)

    # Create buttons
    back_btn = Gtk.Button(label="Back")
    forward_btn = Gtk.Button(label="Forward")

    # Create Url Bar
    url_bar = Gtk.Entry()
    url_bar.connect("activate", search)

    # Organize Grid
    grid.add(back_btn)
    grid.add(forward_btn)
    grid.add(url_bar)
