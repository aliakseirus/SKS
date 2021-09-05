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
import pandas as pd


# download Datastream price
def download_datastream():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')

    if not os.path.isfile('Datastream_price.xls'):
        try:
            site = urllib.request.urlopen("https://datastream.by/files/Datastream_price.xls").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/Datastream_price.xls', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Datastream price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong!')


# download Avant Video price
def download_avant_video():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')
    
    if not os.path.isfile('/home/' + str(os.environ.get( "USERNAME" )) + 
        '/Documents/Prices/avant-tehno-prais-list-video.xlsx'):
        try:
            site = urllib.request.urlopen("https://avant.by/upload/iblock/529/"
                "avant_tehno_prais_list_video.xlsx").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/avant-tehno-prais-list-video.xlsx', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Avant Video price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong! I think, tnat '
                'Avant change way to price again.')


# download Avant Skd price
def download_avant_skd():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')
    
    if not os.path.isfile('/home/' + str(os.environ.get( "USERNAME" )) + 
        '/Documents/Prices/avant-tehno-prais-list-dostup.xlsx'):
        try:
            site = urllib.request.urlopen("https://avant.by/upload/iblock/4f1/"
                "avant_tehno_prais_list_dostup.xlsx").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/avant-tehno-prais-list-dostup.xlsx', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Avant Skd price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong! I think, tnat '
                'Avant change way to price again.')


# download Netair price
def download_netair():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')

    if not os.path.isfile('/home/' + str(os.environ.get( "USERNAME" )) + 
        '/Documents/Prices/price_netair_b2b_sp.xls'):
        try:
            site = urllib.request.urlopen("https://netair.by/price/price_no_data/"
                "price_netair_b2b_sp.xls").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/price_netair_b2b_sp.xls', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Netair price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong!')


# delete folder with prices
def delete_prices():
    try:
        shutil.rmtree('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')
        messagebox.showinfo('Good!', 'All prices has been removed!')
    except:
        messagebox.showinfo('Ohh!', 'There is no folder with prices!')


# closing program
def close_program():
    root.quit()


# get information from enter fields
def get_input():
    
    # check of datastream price
    try:
        datastream_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/Datastream_price.xls')
    except:
        download_datastream()

    # check of avant video price
    try:
        avant_video_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/avant-tehno-prais-list-video.xlsx')
    except:
        download_avant_video()

    # check of avant skd price
    try:
        avant_skd_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/avant-tehno-prais-list-dostup.xlsx')
    except:
        download_avant_skd()

    # check of netair price
    try:
        netair_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/price_netair_b2b_sp.xls')
    except:
        download_netair()

    print('All')

# create program window
root = Tk()
root.attributes('-zoomed',True)
root.title('First Number')
root.iconphoto(True, PhotoImage(file='/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Logo/logo_fn.png'))

# create menu
main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label = 'Datastream Price', command = download_datastream)
file_menu.add_command(label = 'Avant Video Price', command = download_avant_video)
file_menu.add_command(label = 'Avant Skd Price', command = download_avant_skd)
file_menu.add_command(label = 'Netair Price', command = download_netair)
file_menu.add_separator()
file_menu.add_command(label = 'Delete all prices', command = delete_prices)

main_menu.add_cascade(label = 'PRICES', menu = file_menu)
main_menu.add_command(label = 'SKS', command = get_input)
main_menu.add_command(label = 'EXIT', command = close_program)

root.config(menu = main_menu)


# create tabs
tab = ttk.Notebook(root)

tab1 = ttk.Frame(tab)
tab.add(tab1, text = 'Materials')
tab.pack(fill = 'both', expand = True)


# variables
pos = 0             # count of materials
width_of_entry = 3  # width of field


# fill first tab
left_1 = 0          # first column from left side
left_2 = 150         # second column from left side 
line = 0            # index of first line
step = 20           # step of line

lbl = Label(tab1, text = 'UTP/FTP/COAX', fg='red').place(x = left_1, y = line)
line += step


check_utp5e = BooleanVar()
Checkbutton(tab1, 
    text = 'UTP 5e', 
    variable = check_utp5e).place(x = left_1, y = line)
enter_utp5e = Entry(tab1, width = width_of_entry)
enter_utp5e.place(x = left_2, y = line)
line += step

check_utp5e_lszh = BooleanVar()
Checkbutton(tab1, 
    text = 'UTP 5e LSZH', 
    variable = check_utp5e_lszh).place(x = left_1, y = line)
enter_utp5e_lszh = Entry(tab1, width = width_of_entry)
enter_utp5e_lszh.place(x = left_2, y = line)
line += step


# launch program window
root.mainloop()