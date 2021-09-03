# This program can find prices on materials from user's inputs, 
#
# and put it in Excel file.
#
# Program create only for First Number LLC usage.


# import libraries
from tkinter import *
from tkinter import ttk
from tkinter import Radiobutton
from tkinter import Checkbutton
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox
import os
import urllib.request
import shutil


# download Datastream price
def download_datastream():
    if os.path.exists('Prices'):
        pass
    else:
        os.mkdir('Prices')
    
    try:
        site = urllib.request.urlopen("https://datastream.by/files/"
            "Datastream_price.xls").read()
        file = open('Prices/Datastream_price.xls', 'wb')
        file.write(site)
        file.close()
        messagebox.showinfo('Good!', 'Datastream price has beed downloaded!')
    except:
        messagebox.showinfo('Warning!', 'Something went wrong!')


# download Avant Video price
def download_avant_video():
    if os.path.exists('Prices'):
        pass
    else:
        os.mkdir('Prices')
    
    try:
        site = urllib.request.urlopen("https://avant.by/upload/iblock/529/"
            "avant_tehno_prais_list_video.xlsx").read()
        file = open('Prices/avant-tehno-prais-list-video.xlsx', 'wb')
        file.write(site)
        file.close()
        messagebox.showinfo('Good!', 'Avant Video price has beed downloaded!')
    except:
        messagebox.showinfo('Warning!', 'Something went wrong! I think, tnat '
            'Avant change way to price again.')


# download Avant Skd price
def download_avant_skd():
    if os.path.exists('Prices'):
        pass
    else:
        os.mkdir('Prices')
    
    try:
        site = urllib.request.urlopen("https://avant.by/upload/iblock/4f1/"
            "avant_tehno_prais_list_dostup.xlsx").read()
        file = open('Prices/avant-tehno-prais-list-dostup.xlsx', 'wb')
        file.write(site)
        file.close()
        messagebox.showinfo('Good!', 'Avant Skd price has beed downloaded!')
    except:
        messagebox.showinfo('Warning!', 'Something went wrong! I think, tnat '
            'Avant change way to price again.')


# download Netair price
def download_netair():
    if os.path.exists('Prices'):
        pass
    else:
        os.mkdir('Prices')
    
    try:
        site = urllib.request.urlopen("https://netair.by/price/price_no_data/"
            "price_netair_b2b_sp.xls").read()
        file = open('Prices/price_netair_b2b_sp.xls', 'wb')
        file.write(site)
        file.close()
        messagebox.showinfo('Good!', 'Netair price has beed downloaded!')
    except:
        messagebox.showinfo('Warning!', 'Something went wrong!')


# delete folder with prices
def delete_prices():
    try:
        shutil.rmtree('Prices')
        messagebox.showinfo('Good!', 'All prices has been removed!')
    except:
        messagebox.showinfo('Ohh!', 'There is no folder with prices!')


# create program window
root = Tk()
root.title('First Number')

# create menu
main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label='Datastream Price', command=download_datastream)
file_menu.add_command(label='Avant Video Price', command=download_avant_video)
file_menu.add_command(label='Avant Skd Price', command=download_avant_skd)
file_menu.add_command(label='Netair Price', command=download_netair)
file_menu.add_separator()
file_menu.add_command(label='Delete all prices', command=delete_prices)

main_menu.add_cascade(label='PRICES', menu=file_menu)
main_menu.add_cascade(label='SKS', command=None)
main_menu.add_cascade(label='EXIT', command=None)

root.config(menu = main_menu)


# launch program window
root.mainloop()