# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports

def back():
    print("back")


def forward():
    print("forward")


def search(url_box, frame):
    url = url_box.get()
    frame.load_website(url)
    return frame
