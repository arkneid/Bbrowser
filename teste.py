#!/usr/bin/env python3
# coding=utf-8

#########################
# Author: João Chaminé  #
#########################


import gi

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

window = Gtk.Window()
window.set_default_size(800, 600)
window.connect("destroy", Gtk.main_quit)

scrolled_window = Gtk.ScrolledWindow()
webview = WebKit2.WebView()
webview.load_uri("https://google.cl")
scrolled_window.add(webview)

window.add(scrolled_window)
window.show_all()
Gtk.main()
