# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports

def back(widget):
    print("back")


def forward(widget):
    print("forward")


def search(widget, url_bar, frame):
    address = url_bar.get_text()
    if address.startswith("www.") or address.startswith("https://"):
        url_bar.set_text(address)
    else:
        address = "www." + address
        url_bar.set_text(address)

    if address.startswith("https://"):
        frame.load_uri(address)
    else:
        address = "https://" + address
        url_bar.set_text(address)
        frame.load_uri(address)
