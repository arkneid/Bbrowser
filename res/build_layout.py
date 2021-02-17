# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
from gi.repository import Gtk
from res.create_webview import create_frame
from res.buttons_actions import *


def build(window):
    grid = Gtk.Grid()
    window.add(grid)

    # Create Scroll window
    win_scroll = Gtk.ScrolledWindow()
    frame = create_frame()
    win_scroll.add(frame)
    win_scroll.set_hexpand(True)
    win_scroll.set_vexpand(True)

    # Create Url Bar
    url_bar = Gtk.Entry()
    url_bar.connect("activate", search, url_bar, frame)
    url_bar.set_hexpand(True)

    # Create buttons
    back_btn = Gtk.Button(label="Back")
    back_btn.connect("clicked", back)

    forward_btn = Gtk.Button(label="Forward")
    forward_btn.connect("clicked", forward)

    search_btn = Gtk.Button(label="Search")
    search_btn.connect("clicked", search, url_bar, frame)

    # Organize Grid
    grid.attach(back_btn, 0, 0, 1, 1)
    grid.attach(forward_btn, 1, 0, 1, 1)
    grid.attach(url_bar, 2, 0, 1, 1)
    grid.attach(search_btn, 3, 0, 1, 1)
    grid.attach(win_scroll, 0, 1, 4, 1)
