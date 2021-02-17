# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
import gi

gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2


def create_frame():
    frame = WebKit2.WebView()
    frame.load_uri("")
    return frame
