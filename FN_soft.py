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


# download Datastream price





# create program window
root = Tk()
root.title('First Number')

# create menu
main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label='Datastream Price', command=None)
file_menu.add_command(label='Avant Video Price', command=None)
file_menu.add_command(label='Avant Skd Price', command=None)
file_menu.add_command(label='Netair Price', command=None)
file_menu.add_separator()
file_menu.add_command(label='Delete all prices', command=None)

main_menu.add_cascade(label='PRICES', menu=file_menu)
main_menu.add_cascade(label='SKS', command=None)
main_menu.add_cascade(label='EXIT', command=None)

root.config(menu = main_menu)


# launch program window
root.mainloop()