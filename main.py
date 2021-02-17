#!/usr/bin/env python3
# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from res.build_layout import build

# Build main window

window = Gtk.Window(title="Bbrowser")
window.set_default_size(800, 600)
window.connect("destroy", Gtk.main_quit)

build(window)

window.show_all()
Gtk.main()
